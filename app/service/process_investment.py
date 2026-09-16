from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject, Donation
from app.models.base import InvestBase

GET_SOURCES_BY_TYPE = {
    Donation: charity_project_crud.get_uninvested_objects,
    CharityProject: donation_crud.get_uninvested_objects,
}


async def process_investment(
    target: InvestBase,
    session: AsyncSession,
):
    update_sources = []
    get_sources = GET_SOURCES_BY_TYPE.get(type(target))
    sources = await get_sources(session)
    for source in sources:
        update_sources.append(source)
        amount_to_invest = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount,
        )
        for object in (target, source):
            object.invested_amount += amount_to_invest
            object.close_fund()
        if target.fully_invested:
            break
        update_sources.append(source)
    target.close_fund()
    session.add_all(update_sources)
    await session.commit()
    return target
