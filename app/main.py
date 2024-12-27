from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from app.core.database import get_db
from app.api.v1.api_v1 import api_router as v1_router

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users.",
    },
    {
        "name": "random",
        "description": "Random number generators",
    },
    {
        "name": "healthcheck",
        "description": "Perform a Health Check",
    },
]

app = FastAPI(title="MyAPI",
              summary="My very first API",
              version="0.2.0",
              contact={"name": "Me",
                       "url": "http://justme.ai/contact/",
                       "email": "me@mail.com",
                       },
              license_info={"name": "Apache 2.0",
                            },
              openapi_tags=tags_metadata
              )

app.include_router(v1_router, prefix="/v1")


@app.get("/health",
         tags=["healthcheck"],
         response_model=dict,
         )
async def get_health(db: AsyncSession = Depends(get_db)):
    try:
        # Check the connection to the database
        await db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception:  # as e:
        # print(f"{type(e).__name__}
        # at line {e.__traceback__.tb_lineno}
        # of {__file__}: {e}")
        raise HTTPException(status_code=503,
                            detail="Database connection failed"
                            )


@app.get("/")
def welcome():
    return {"message": "Welcome to the FastAPI project! :3"}
