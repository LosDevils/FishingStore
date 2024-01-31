from inventory.domain.interfaces.i_unit_of_work import IUnitOfWork
from inventory.infrastructure.utils.repositories import ProductRepository, \
    CategoryRepository, SubCategoryRepository, CharacteristicRepository, \
    CharacteristicTypeRepository


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.product = ProductRepository(self.session)
        self.category = CategoryRepository(self.session)
        self.sub_category = SubCategoryRepository(self.session)
        self.characteristic = CharacteristicRepository(self.session)
        self.characteristic_type = CharacteristicTypeRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.commit()
