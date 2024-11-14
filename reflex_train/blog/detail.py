import reflex as rx

from . import state
from ..ui.base import base_page

# @rx.page(route=routes.ABOUT_US_ROUTE)
def blog_post_detail_page() -> rx.Component:
    # About Us Page
    my_child = rx.vstack(
        rx.heading(state.BlogPostState.post.title, size="9"),
        rx.text(
            state.BlogPostState.post.content
        ),
        spacing="5",
        justify="center",
        align='center',
        min_height="85vh"
    )

    return base_page(my_child)