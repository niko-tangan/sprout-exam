from typing import Any, List
from fastapi import FastAPI, Depends, HTTPException, Query, WebSocket

from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import ScalarResult
from sqlmodel import SQLModel, Session, select
from .models.employee import *

# from starlette.middleware import Middleware
# from starlette.middleware.cors import CORSMiddleware

# from .models.models import *
from .db import *
from contextlib import asynccontextmanager
from .config import Settings, get_settings
from typing_extensions import Annotated


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    await Employee.seed_employees()
    yield
    print("Application Ended")


# middleware = [
#     Middleware(
#         CORSMiddleware,
#         allow_origins=["*"],
#         allow_credentials=True,
#         allow_methods=["GET", "POST"],
#         allow_headers=["*"],
#     )
# ]

app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = (
        "https://localhost:5173, http://localhost:5173, http://localhost:3000"
    )
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


origins = [
    "https://localhost:5173",
    "http://localhost:5173",
    "http://localhost:5173/",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["*"],
# )


@app.post("/employees/", response_model=EmployeePublic)
async def create_employee(
    employee: EmployeeCreate, session: Session = Depends(get_session)
) -> Employee:
    db_employee = Employee.model_validate(employee)
    session.add(db_employee)
    session.commit()
    session.refresh(db_employee)
    return db_employee


@app.get("/employees", response_model=list[EmployeePublic])
async def read_employees(session: Session = Depends(get_session)):
    return session.exec(select(Employee)).all()


@app.get("/employees/{employee_id}", response_model=EmployeePublic)
async def read_employee(employee_id: int, session: Session = Depends(get_session)):
    if employee := session.get(Employee, employee_id):
        return employee
    raise HTTPException(status_code=404, detail="Employee not found")


@app.patch("/employees/{employee_id}", response_model=EmployeePublic)
def update_employee(employee_id: int, employee: EmployeeUpdate):
    with Session(engine) as session:
        if db_employee := session.get(Employee, employee_id):
            employee_data = employee.model_dump(exclude_unset=True)
            db_employee.sqlmodel_update(employee_data)
            session.add(db_employee)
            session.commit()
            session.refresh(db_employee)
            return db_employee
        raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, session: Session = Depends(get_session)):
    if to_delete := session.get(Employee, employee_id):
        session.delete(to_delete)
        session.commit()
        return {"ok": True}
    raise HTTPException(status_code=404, detail="Employee not found")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:

        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"{data}")
