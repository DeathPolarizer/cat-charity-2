from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class DonationBase(BaseModel):
    full_amount: int = Field(gt=0)
    comment: str | None = None

    model_config = ConfigDict(extra="forbid")


class DonationCreate(DonationBase):
    pass


class DonationDB(DonationBase):
    id: int
    create_date: datetime


class DonationFullInfoDB(DonationDB):
    invested_amount: int
    fully_invested: bool
    user_id: int
    close_date: datetime | None = None
