from typing import List, Optional

import reflex as rx
from sqlmodel import select

from .model import BlogPostModel

class BlogPostState(rx.State):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None

    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
            ).all()
            self.posts = result

    def add_posts(self,form_data:dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            print("adding ", post)
            session.add(post)
            session.commit()
            session.refresh(post) #post.id
            self.post = post

    def get_post(self):
        pass

class BlogAddPostFormState(BlogPostState):
    form_data:dict = {}

    def handle_submit(self,form_data):
        self.form_data = form_data
        self.add_posts(form_data)