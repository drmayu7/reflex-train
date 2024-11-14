from datetime import datetime
import sqlalchemy

import reflex as rx
from sqlmodel import Field

from .. import utils

class ContactEntryModel(rx.Model,table=True):
    user_id:int | None = None
    first_name:str
    last_name:str = Field(nullable=True,default=None)
    email:str = Field(nullable=True,default=None)
    message:str
    created_at: datetime = Field(default_factory=utils.timing.get_utc_now,
                                 nullable=False,
                                 sa_type=sqlalchemy.DateTime(timezone=True),
                                 sa_column_kwargs={
                                     "server_default": sqlalchemy.func.now()
                                        },
                                 )