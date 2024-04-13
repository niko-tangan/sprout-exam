from sqlalchemy import Engine, delete
from sqlmodel import Session, create_engine, select
from .config import get_settings

db_uri = get_settings().db_uri
engine = create_engine(db_uri, echo=True)


async def get_engine() -> Engine:
    return engine


# @app.get("/env")
# async def env(settings: Annotated[Settings, Depends(get_settings)]):
#     return {
#         "app_name": settings.app_name,
#         "admin_username": settings.admin_username,
#         "admin_password": settings.admin_password,
#     }
