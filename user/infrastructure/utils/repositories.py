from user.infrastructure.database.repository import Repository
from user.infrastructure.database.models.user import UserOrm



class UserRepository(Repository):
    model = UserOrm
    adapter = UserAdapter
