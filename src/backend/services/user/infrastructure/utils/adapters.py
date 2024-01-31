from user.domain.interfaces.i_adapter import IAdapter
from user.domain.models.user import User
from user.infrastructure.database.models.user import UserOrm


class UserAdapter(IAdapter):
    @classmethod
    async def to_domain_model(cls, orm_model: UserOrm):
        return User(uuid=orm_model.uuid,
                    username=orm_model.username,
                    balance=orm_model.balance,
                    email=orm_model.email,
                    phone_number=orm_model.phone_number,
                    hashed_password=orm_model.hashed_password)

    @classmethod
    async def to_orm_model(cls, domain_model: User):
        return UserOrm(uuid=domain_model.uuid,
                       username=domain_model.username,
                       balance=domain_model.balance,
                       email=domain_model.email,
                       phone_number=domain_model.phone_number,
                       hashed_password=domain_model.hashed_password)
