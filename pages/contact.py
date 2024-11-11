import reflex as rx
import asyncio

from ui.base import base_page
from navigation import routes

class ContactEntryModel(rx.Model,table=True):
    first_name:str
    last_name:str
    email:str
    message:str

class ContactState(rx.State):
    form_data:dict = {}
    did_submit:bool = False
    timeleft:int = 5

    @rx.var
    def timeleft_label(self):
        if self.timeleft < 1:
            return "Time's up!"
        return f"Time left: {self.timeleft} seconds"

    @rx.var
    def thank_you(self):
        username = self.form_data.get("first_name") or ""
        return f"Thank you {username}".strip() + " for your submission!"

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data
        self.did_submit = True
        yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield

    async def countdown(self):
        while self.timeleft > 0:
            await asyncio.sleep(1)
            self.timeleft -= 1
            yield

@rx.page(route=routes.CONTACT_US_ROUTE,on_load=ContactState.countdown)
def contact_page() -> rx.Component:
    my_form = rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                name="first_name",
                placeholder="First Name",
                required=True,
                width="100%",
            ),
            rx.input(
                name="last_name",
                placeholder="Last Name",
                required=True,
                width="100%",
            ),
                width="100%"
            ),
            rx.input(
                name="email",
                type="email",
                placeholder="Your Email",
                required=True,
                width="100%",
            ),
            rx.text_area(
                name="message",
                placeholder="Your message",
                required=True,
                width="100%",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=ContactState.handle_submit,
        reset_on_submit=True,
    )

    my_child = rx.vstack(
        rx.heading('Contact Form', size="9"),
        rx.text(
            "Contact us now!",
        ),
        rx.text(ContactState.timeleft_label),
        rx.cond(ContactState.did_submit,ContactState.thank_you,""),
        rx.desktop_only(
            rx.box(
                my_form,
                width="50vw",
            )
        ),
        rx.mobile_and_tablet(
            rx.box(
                my_form,
                width="80vw",
            )
        ),
        spacing="5",
        justify="center",
        align='center',
        min_height="85vh",
        id='my-child-pricing'
    )

    return base_page(my_child)