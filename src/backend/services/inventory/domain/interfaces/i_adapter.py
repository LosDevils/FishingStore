from abc import ABC, abstractmethod


class IAdapter(ABC):
    @classmethod
    @abstractmethod
    async def to_domain_model(cls, orm_model):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    async def to_orm_model(cls, domain_model):
        raise NotImplementedError
