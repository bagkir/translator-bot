from sqlalchemy import Integer, String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=False)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    language: Mapped[str] = mapped_column(default='en')
    translate_mode: Mapped[bool] = mapped_column(default=False)
    tg_id: Mapped[int] = mapped_column(BigInteger, nullable=True)
