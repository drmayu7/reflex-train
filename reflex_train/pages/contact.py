# import reflex as rx
#
# from contact.form import contact_form
# from contact.state import ContactState
# from ui.base import base_page
# from navigation import routes
#
# @rx.page(route=routes.CONTACT_US_ROUTE,
#          # on_load=ContactState.countdown # uncomment this line to start the countdown
#          )
# def contact_page() -> rx.Component:
#     my_child = rx.vstack(
#         rx.heading('Contact Form', size="9"),
#         rx.text(
#             "Contact us now!",
#         ),
#         # rx.text(ContactState.timeleft_label),
#         rx.cond(ContactState.did_submit,ContactState.thank_you,""),
#         rx.desktop_only(
#             rx.box(
#                 contact_form(),
#                 width="50vw",
#             )
#         ),
#         rx.mobile_and_tablet(
#             rx.box(
#                 contact_form(),
#                 width="80vw",
#             )
#         ),
#         spacing="5",
#         justify="center",
#         align='center',
#         min_height="85vh",
#         id='my-child-pricing'
#     )
#
#     return base_page(my_child)
#
