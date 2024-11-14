import reflex as rx

from . import state

def blog_post_add_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                name="title",
                placeholder="Title",
                required=True,
                width="100%",
            ),
                width="100%"
            ),
            rx.text_area(
                name="content",
                placeholder="Add content here",
                height='50vh',
                width="100%",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=state.BlogAddPostFormState.handle_submit,
        reset_on_submit=True,
    )