from sqlalchemy import select

from app.dao.base import BaseDAO
from app.models.users import User


class UsersDAO(BaseDAO):
    model = User

    @classmethod
    def get_user(cls, session, user_id):
        return session.execute(select(User).where(User.id == user_id)).scalar_one()
