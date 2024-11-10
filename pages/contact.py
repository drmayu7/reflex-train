import reflex as rx

from ui.base import base_page
from navigation import routes

@rx.page(route=routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    # About Us Page
    my_child = rx.vstack(
        rx.heading('Contact', size="9"),
        rx.text(
            "Contact us now!",
        ),
        spacing="5",
        justify="center",
        align='center',
        min_height="85vh",
        id='my-child-pricing'
    )

    return base_page(my_child)