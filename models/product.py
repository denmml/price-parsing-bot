
from sqlalchemy import datetime, Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Product(Base):
    __tablename__ = "products"

    #основные поля таблицы
    id: Mapped[int] = mapped_column(primary_key = True,
                                    autoincrement=True)
    url: Mapped[str] = mapped_column(String(2048), unique = True,
                                     index = True, nullable = False)
    title: Mapped[str] = mapped_column(String(512), nullable = False)
    current_price: Mapped[Float] = mapped_column(Float, nullable = False)

    