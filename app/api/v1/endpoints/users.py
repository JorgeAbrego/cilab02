from typing import List, Union
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import get_db
from app.api.v1.models.users import User
from app.api.v1.schemas.users import UserBase
from app.api.v1.schemas.users import UserCreate
from app.core.logger import setup_logger
from app.core.crypt import get_hash

logger = setup_logger("v1")

router = APIRouter()


def get_password_hash(password):
    return get_hash(password)


# Endpoint to get all users
@router.get("/", response_model=Union[List[UserBase], dict],
            tags=["users"])
async def get_users(db: AsyncSession = Depends(get_db)):
    logger.info("Listing users required")
    result = await db.execute(select(User))
    users = result.scalars().all()

    if not users:
        # Returns a message if there are no records
        logger.warn("No users found in table")
        return {"message": "No hay usuarios registrados en la base de datos"}

    # Returns the list of users transformed into Pydantic objects
    logger.info("Users listed successfully")
    return [UserBase.from_orm(user) for user in users]


# Endpoint to create a user
@router.post("/",
             response_model=dict,
             status_code=status.HTTP_201_CREATED,
             tags=["users"])
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"Someone is creating a new user {user.username}")

    # Check if the user already exists in the database
    # db_user = db.query(User).filter(User.username == user.username).first()
    result = await db.execute(select(User)
                              .where(User.username == user.username)
                              )
    db_user = result.scalars().first()
    if db_user:
        logger.warning(f"Attempt to create an existing user: {user.username}")
        raise HTTPException(status_code=400,
                            detail="Username already registered")
    # Check if the email already exists in the database
    # db_email = db.query(User).filter(User.email == user.email).first()
    result = await db.execute(select(User).where(User.email == user.email))
    db_email = result.scalars().first()
    if db_email:
        raise HTTPException(status_code=400,
                            detail="Email already registered")

    # Create a new user with the encrypted password
    new_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=get_password_hash(user.password),
        role=user.role
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    msg = f"New user {new_user.username} created successfully by someone"
    logger.info(msg)
    return {"message": "User created successfully",
            "username": new_user.username
            }
