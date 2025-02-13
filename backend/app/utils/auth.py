import datetime

from passlib.context import CryptContext

from jose import jwt

from app.config import settings
from app.dao.overlays import OverlaysDAO
from app.dao.users import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def authenticate_user(session, user_info: dict):
    user_id = user_info.get("id")
    if user_id:
        user_db = await UsersDAO.find_by_twitch_id(session, user_id)

        if not user_db:
            user_db = await UsersDAO.add(
                session,
                username=user_info["login"],
                avatar_url=user_info["profile_image_url"],
                twitch_id=user_info["id"],
                twitch_display_name=user_info["display_name"],
            )

            await OverlaysDAO.add(session, user_id=user_db.id)
        return user_db
    else:
        return None
