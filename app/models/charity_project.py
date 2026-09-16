from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.constants import NAME_LENGTH_DB
from app.models.base import InvestBase


class CharityProject(InvestBase):
    name: Mapped[str] = mapped_column(
        String(NAME_LENGTH_DB),
        unique=True,
        nullable=False,
    )
    description: Mapped[str] = mapped_column(Text, nullable=False)

    def __repr__(self) -> str:
        base_repr = super().__repr__()
        return f"{base_repr}\nname={self.name}"
