from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import ScalarResult
from sqlmodel import SQLModel, Session, select
from .models import Employee
from .db import get_engine
from contextlib import asynccontextmanager
from .config import Settings, get_settings
from typing_extensions import Annotated


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = await get_engine()
    SQLModel.metadata.create_all(engine)
    await Employee.seed_employees()
    yield
    await Employee.delete_all()
    print("Application Ended")


app = FastAPI(lifespan=lifespan)


@app.get("/employees")
async def employees():
    result: ScalarResult = await Employee.get_all()
    employees = {
        r.email: {
            "full_name": f"{r.first_name} {r.last_name}",
            "first_name": r.first_name,
            "last_name": r.last_name,
        }
        for r in result
    }
    return employees


@app.get("/employees/{employee_id}")
async def read_employee(employee_id: int):
    return await Employee.get(employee_id)


@app.delete("/employees/delete/{employee_id}")
async def delete_employee(employee_id: int):
    return await Employee.delete(employee_id)
