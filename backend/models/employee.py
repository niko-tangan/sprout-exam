from typing import Self
from fastapi import Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import ScalarResult
from sqlmodel import Field, SQLModel, Session, select

from backend.models.models import Model

from ..db import get_engine, get_session


class EmployeeBase(SQLModel):
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    email: str


class Employee(Model, table=True):
    __tablename__ = "employees"

    id: int | None = Field(default=None, primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    email: str

    @classmethod
    async def seed_employees(cls):
        employees = [
            {
                "first_name": "Liam",
                "last_name": "Byrne",
                "email": "brimstone@vprotocol.com",
            },
            {
                "first_name": "Sabine",
                "last_name": "Callas",
                "email": "viper@vprotocol.com",
            },
            {
                "first_name": "Lingying",
                "last_name": "Wei",
                "email": "sage@vprotocol.com",
            },
            {
                "first_name": "Jamie",
                "last_name": "Adeyemi",
                "email": "phoenix@vprotocol.com",
            },
        ]
        with Session(await get_engine()) as session:
            for employee in employees:
                print(employee)
                session.add(
                    cls(
                        first_name=employee.get("first_name"),
                        last_name=employee.get("last_name"),
                        email=employee.get("email"),
                    )
                )
            session.commit()


class EmployeePublic(EmployeeBase):
    id: int


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
