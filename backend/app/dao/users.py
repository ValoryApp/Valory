from sqlalchemy import select

from app.dao.base import BaseDAO
from app.models.users import User


class UsersDAO(BaseDAO):
    model = User

    @classmethod
    async def find_by_twitch_id(cls, session, twitch_id):
        query = select(cls.model).filter_by(twitch_id=twitch_id)
        result = await session.execute(query)
        return result.scalars().one_or_none()
