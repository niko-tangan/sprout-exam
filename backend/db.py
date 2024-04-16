from sqlalchemy import Engine, delete
from sqlmodel import SQLModel, Session, create_engine, select
from .config import get_settings

db_uri = get_settings().db_uri
connect_args = {"check_same_thread": False}
engine = create_engine(db_uri, echo=True, connect_args=connect_args)


def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


async def get_engine() -> Engine:
    return engine


async def get_session():
    with Session(engine) as session:
        yield session


# @app.get("/env")
# async def env(settings: Annotated[Settings, Depends(get_settings)]):
#     return {
#         "app_name": settings.app_name,
#         "admin_username": settings.admin_username,
#         "admin_password": settings.admin_password,
#     }
