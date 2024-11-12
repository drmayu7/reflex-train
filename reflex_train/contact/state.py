import reflex as rx
import asyncio

from reflex_train.contact.model import ContactEntryModel

class ContactState(rx.State):
    form_data:dict = {}
    did_submit:bool = False


    @rx.var
    def thank_you(self):
        username = self.form_data.get("first_name") or ""
        return f"Thank you {username}".strip() + " for your submission!"

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        # print(form_data)
        self.form_data = form_data
        data = {} #change to validate using pydantic later
        for k,v in form_data.items(): #
            if v == "" or v is None: #
                continue #
            data[k] = v #

        with rx.session() as session:
            db_entry = ContactEntryModel(**data)
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield
        await asyncio.sleep(6)
        self.did_submit = False
        yield

    # async def countdown(self):
    #     while self.timeleft > 0:
    #         await asyncio.sleep(1)
    #         self.timeleft -= 1
    #         yield