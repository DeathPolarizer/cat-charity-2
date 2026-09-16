from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import InvestBase


class Donation(InvestBase):
    comment: Mapped[str] = mapped_column(Text, nullable=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("user.id", name="fk_donation_user_id_user"),
    )

    def __repr__(self) -> str:
        base_repr = super().__repr__()
        return f"{base_repr}\ncomment={self.comment}\nuser={self.user_id}"
