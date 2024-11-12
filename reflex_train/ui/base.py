import reflex as rx

from .nav import nav_bar

def base_page(child:rx.Component,hide_navbar=False,*args,**kwargs) -> rx.Component:
    # print([type(x) for x in args])
    if not isinstance(child,rx.Component):
        child = rx.heading('Error: child must be a reflex component')
    if hide_navbar:
        return rx.container(
            child,# This component is dynamic and changes for each page
            rx.logo(), # This component is static for all pages
            rx.color_mode.button(position="bottom-right"),# This component is static for all pages
            id='my-base-container'
        )
    return rx.fragment(
        nav_bar(),
        rx.box(
            child,  # This component is dynamic and changes for each page
            id='my-content-area-el',
            # bg=rx.color("accent", 3),
            padding="1em",
            width="100%"
        ),
        rx.logo(),  # This component is static for all pages
        rx.color_mode.button(position="bottom-right"),  # This component is static for all pages
        id='my-base-container'
    )