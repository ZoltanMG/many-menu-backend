from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from flask_login import UserMixin


class User(UserMixin, BaseModel, Base):
    __tablename__ = 'user'

    email = Column(String(60), nullable=False)
    pwd = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
