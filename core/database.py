
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from core.config import Settings


#Создаем асинхронный движок для подключения к postgresql
async_engine = create_async_engine(
    str(Settings.DATABASE_URL),
    echo = True, 
    future=True,

)

#Фабрика сессий(нужна для создания транзакций)
AsyncSessionLocal = async_sessionmaker(
    bind = async_engine,
    expire_on_commit=False,

)

#ф-ция-зависимость для FastApi(будем отдавать сессию в эндпоинты)
async def get_dg():
    async with AsyncSessionLocal() as session:
        yield session
        