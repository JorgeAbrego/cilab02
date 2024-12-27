import asyncio
from app.core.database import engine, Base
# Import all your models here
from app.api.v1.models import users  # noqa: F401


async def init_db():
    async with engine.begin() as conn:
        print("Inicializando la base de datos...")
        # Drop if necessary: await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Base de datos inicializada correctamente.")


if __name__ == "__main__":
    asyncio.run(init_db())
