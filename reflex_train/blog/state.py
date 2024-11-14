from typing import List, Optional

import reflex as rx
from sqlalchemy import update
from sqlmodel import select

from .model import BlogPostModel


class BlogPostState(rx.State):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None
    post_content: str = ''

    @rx.var
    def blog_post_id(self):
        return self.router.page.params.get('blog_id','')

    def get_post_detail(self):
        with rx.session() as session:
            if self.blog_post_id == '':
                self.post = None
                return
            result = session.exec(
                select(BlogPostModel).where(
                    BlogPostModel.id == self.blog_post_id
                )
            ).one_or_none()
            self.post = result
            self.post_content = self.post.content

    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
            ).all()
            self.posts = result

    def add_posts(self,form_data:dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            # print("adding ", post)
            session.add(post)
            session.commit()
            session.refresh(post) #post.id
            # print("added ", post)
            self.post = post

    def save_post_edits(self,post_id:int,updated_data:dict):
        with rx.session() as session:
            post = session.exec(
                select(BlogPostModel).where(
                    BlogPostModel.id == post_id
                )
            ).one_or_none()
            if post is None:
                return
            for key,value in updated_data.items():
                setattr(post,key,value)
            session.add(post)
            session.commit()
            session.refresh(post)

    def get_post(self):
        pass

class BlogAddPostFormState(BlogPostState):
    form_data:dict = {}

    def handle_submit(self,form_data):
        self.form_data = form_data
        self.add_posts(form_data)

class BlogEditPostFormState(BlogPostState):
    form_data:dict = {}
    #post_content:str = "" - from BlogPostState

    def handle_submit(self,form_data):
        self.form_data = form_data
        post_id = form_data.pop('post_id')
        updated_data = {**form_data}
        print(post_id,updated_data)
        self.save_post_edits(post_id,updated_data)