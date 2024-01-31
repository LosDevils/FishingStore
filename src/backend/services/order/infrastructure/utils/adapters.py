from order.domain.interfaces.i_adapter import IAdapter
from order.domain.models.order import Order
from order.infrastructure.database.models.order import OrderOrm


class OrderAdapter(IAdapter):
    @classmethod
    async def to_domain_model(cls, orm_model: OrderOrm):
        return Order(id=orm_model.id,
                     products_id=orm_model.products_id,
                     user_id=orm_model.user_id,
                     status=orm_model.status,
                     created_at=orm_model.created_at)

    @classmethod
    async def to_orm_model(cls, domain_model: Order):
        return OrderOrm(id=domain_model.id,
                        products_id=domain_model.products_id,
                        user_id=domain_model.user_id,
                        status=domain_model.status,
                        created_at=domain_model.created_at)
