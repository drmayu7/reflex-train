"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page


from . import navigation,pages,contact


class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"

    def handle_title_input_change(self, value: str):
        """Handle the input change event."""
        self.label = value

    def did_click(self):
        """Handle the click event."""
        self.label = "Hello, Reflex clicking!"
        print(self.label)
        return rx.redirect(navigation.routes.ABOUT_US_ROUTE)


def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            # rx.button('About Us',on_click=State.did_click),
            rx.link(rx.button('About Us'), href=navigation.routes.ABOUT_US_ROUTE), # for button - always use this type to route link
            spacing="5",
            justify="center",
            text_align="center",
            align='center',
            min_height="85vh",
            id = 'my-child'
        )

    return base_page(my_child,
                     # hide_navbar=True
                     )

app = rx.App()
app.add_page(index, route=navigation.routes.HOME_ROUTE)
app.add_page(contact.contact_page,route=navigation.routes.CONTACT_US_ROUTE)
app.add_page(
    contact.contact_entries_list_page,
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries
)
app.add_page(pages.about_page,route=navigation.routes.ABOUT_US_ROUTE)
app.add_page(pages.pricing_page,route=navigation.routes.PRICING_ROUTE)

