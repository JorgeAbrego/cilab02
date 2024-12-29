from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Creating the database engine
engine = create_async_engine(settings.DB_URL, echo=True)

# Creating an asynchronous session factory
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    # expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# Create the base class for the models
Base = declarative_base()


# Dependency to obtain the database session
async def get_db():
    async with async_session() as session:
        yield session
