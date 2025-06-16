from aiogram.types import User as UserType
from sqlalchemy import select

from app.database import async_session_maker
from app.users.models import User as UserModel


class UserDAO:
    @classmethod
    def user_to_dict(cls, user: UserType, language: str, translate_mode: bool) -> dict:
        return {
            "username": user.username or f"user_{user.id}",
            "first_name": user.first_name or "",
            "last_name": user.last_name or "",
            "language": language,
            "translate_mode": translate_mode,
            "tg_id": user.id
        }

    @classmethod
    async def add_user(cls, user: UserType, language: str, translate_mode: bool):
        async with async_session_maker() as session:
            async with session.begin():
                new_user = UserModel(**cls.user_to_dict(user, language, translate_mode))
                session.add(new_user)
                await session.flush()
                await session.commit()

    @classmethod
    async def find_all(cls, **filters) -> list[UserModel]:
        async with async_session_maker() as session:
            query = select(UserModel).filter_by(**filters)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_by_id(cls, user_id: int):
        async with async_session_maker() as session:
            query = select(UserModel).where(UserModel.id == user_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()