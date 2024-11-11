import reflex as rx
from sqlalchemy.testing.config import db_url

config = rx.Config(
    app_name="reflex_train",
    db_url="sqlite:///reflex_train.db",
)