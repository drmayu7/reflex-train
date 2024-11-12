from datetime import datetime,timezone
import sqlalchemy

import reflex as rx
from sqlmodel import Field

def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)

class ContactEntryModel(rx.Model,table=True):
    first_name:str
    last_name:str = Field(nullable=True,default=None)
    email:str = Field(nullable=True,default=None)
    message:str
    created_at: datetime = Field(default=get_utc_now(),
                                 nullable=False,
                                 sa_type=sqlalchemy.DateTime(timezone=True),
                                 sa_column_kwargs={
                                     "server_default": sqlalchemy.func.now()
                                        },
                                 )