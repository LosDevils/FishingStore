from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker

from inventory.config import DataBaseConfig


class DataBaseService:
    def __init__(self, config: DataBaseConfig):
        self.__config = config
        self.__engine = None

    def create_engine(self) -> AsyncEngine:
        self.__engine = create_async_engine(
            f"postgresql+{self.__config.DB_DRIVER}://{self.__config.DB_USER}:{self.__config.DB_PASS}@"
            f"{self.__config.DB_HOST}:{self.__config.DB_PORT}/{self.__config.DB_NAME}")
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
