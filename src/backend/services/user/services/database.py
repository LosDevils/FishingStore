from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker
from cfg.config import DbConfig


class DataBaseService:
    def __init__(self, config: DbConfig):
        self.__config = config
        self.__engine = None

    def create_engine(self) -> AsyncEngine:
        self.__engine = create_async_engine(
            f"{self.__config.database}+{self.__config.driver}://{self.__config.username}:{self.__config.password}@{self.__config.host}/{self.__config.db_name}")
        return self.__engine

    def get_session(self):
        if self.__engine is None:
            self.create_engine()
        session = AsyncSession(bind=self.__engine)
        return session

    def get_async_session_maker(self):
        if self.__engine is None:
            self.create_engine()
        session_maker = async_sessionmaker(bind=self.__engine)
        return session_maker
