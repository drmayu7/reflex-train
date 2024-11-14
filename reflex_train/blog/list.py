import reflex as rx


from . import state,model
from ..ui.base import base_page
from .. import navigation

def blog_post_detail_link(child: rx.Component,post: model.BlogPostModel):
    if post is None:
        return rx.fragment(child)
    post_id = post.id
    if post_id is None:
        return rx.fragment(child)
    root_path = navigation.routes.BLOG_POSTS_ROUTE
    post_detail_url = f"{root_path}/{post_id}"
    return rx.link(
        child,
    href=post_detail_url)


def blog_posts_list_item(post: model.BlogPostModel):
    return rx.box(
        blog_post_detail_link(
        rx.heading(post.title),
        post

    ),
    padding = "1em",
    )

def blog_post_list_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading('Blog Posts',size="5"),
            rx.link(
                rx.button("New Post"),
                href=navigation.routes.BLOG_POSTS_ADD_ROUTE
                    ),
            # rx.foreach(["abc","abc","ecd"],foreach_callback),
            rx.foreach(state.BlogPostState.posts,blog_posts_list_item),
        spacing="5",
        align='center',
        min_height="85vh",
        id='my-child-entries'
    ))