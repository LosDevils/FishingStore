from order.infrastructure.database.models.order import OrderOrm
from order.infrastructure.utils.adapters import OrderAdapter
from order.infrastructure.database.repository import Repository


class OrderRepository(Repository):
    model = OrderOrm
    adapter = OrderAdapter
