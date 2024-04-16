from datetime import date
from typing import Self
from fastapi import HTTPException
from sqlalchemy import ScalarResult, delete
from sqlmodel import Field, SQLModel, Session, select

from backend.db import get_engine

# from ..db import get_engine


class Model(SQLModel, table=False):
    @classmethod
    async def get(cls, id):
        engine = await get_engine()
        with Session(engine) as session:
            if data := session.get(cls, id):
                return data
            raise HTTPException(status_code=404, detail=f"{cls.__name__} not found")

    @classmethod
    async def get_all(cls, session) -> ScalarResult:
        engine = await get_engine()
        with Session(engine) as session:
            return session.exec(select(cls)).all()

    async def create(cls: Self):
        engine = await get_engine()
        with Session(engine) as session:
            db_cls = cls  # Self.model_validate(cls)
            session.add(db_cls)
            session.commit()
            session.refresh(db_cls)
            return db_cls

    @classmethod
    async def delete(cls, id):
        engine = await get_engine()
        with Session(engine) as session:
            if to_delete := session.get(cls, id):
                session.delete(to_delete)
                session.commit()
                return {"ok": True}
            raise HTTPException(status_code=404, detail=f"{cls.__name__} not found")

    @classmethod
    async def delete_all(cls):
        engine = await get_engine()
        with Session(engine) as session:
            statement = delete(cls)
            session.exec(statement)
            session.commit()


# class Contract(Model, table=True):
#     __tablename__ = "contracts"

#     id: int | None = Field(default=None, primary_key=True)
#     project: str
#     contract_end_date: date
#     employee_id: int | None = Field(default=None, foreign_key="employees.id")


# class Benefit(Model, table=True):
#     # is benefit status a better name?
#     __tablename__ = "benefits"

#     id: int | None = Field(default=None, primary_key=True, foreign_key="employees.id")
#     current_leaves: float = 0
#     max_leaves: float = 1
#     benefits: str | None = None


# class Account(Model, table=True):
#     __tablename__ = "accounts"

#     id: int | None = Field(default=None, primary_key=True, foreign_key="employees.id")
#     username: str
#     password: str
