from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models.user import User
from app.schemas.donation import DonationCreate, DonationDB, DonationFullInfoDB
from app.service import process_investment

router = APIRouter()

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]
SuperUserDep = Depends(current_superuser)
UserDep = Annotated[User, Depends(current_user)]


@router.get(
    "/",
    summary="Получение всех пожертвований",
    response_model=list[DonationFullInfoDB],
    response_model_exclude_none=True,
    dependencies=[SuperUserDep],
)
async def get_all_donations(session: SessionDep):
    return await donation_crud.get_all(session)


@router.get(
    "/my",
    response_model=list[DonationDB],
    response_model_exclude_none=True,
)
async def get_user_donations(
    session: SessionDep,
    user: UserDep,
):
    return await donation_crud.get_user_donation(session, user)


@router.post(
    "/",
    summary="Создание пожертвования",
    response_model=DonationDB,
    response_model_exclude_none=True,
)
async def create_donation(
    donation: DonationCreate,
    session: SessionDep,
    user: UserDep,
):
    donation_db = await donation_crud.create(
        obj_in=donation,
        session=session,
        user=user,
    )
    return await process_investment(donation_db, session)
