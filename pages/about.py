import reflex as rx

from ui.base import base_page
from . import register_page
from navigation import routes

@register_page(routes.ABOUT_US_ROUTE)
# @rx.page(route='/about-us')
def about_page() -> rx.Component:
    # About Us Page
    my_child = rx.vstack(
        rx.heading('About Us', size="9"),
        rx.text(
            "Register with us to get started!",
        ),
        spacing="5",
        justify="center",
        align='center',
        min_height="85vh",
        id='my-child-about-us'
    )

    return base_page(my_child)