import asyncio
from typing import List
from django.shortcuts import aget_object_or_404  # type: ignore
from ninja import NinjaAPI
import time

from employee.models import Department, Employee
from employee.schemas import EmployeeIn, EmployeeOut

api = NinjaAPI()


@api.post("/departments")
async def create_department(request, title: str):
    department = await Department.objects.acreate(title=title)
    return {"id": department.pk}


@api.post("/employees")
async def create_employee(request, payload: EmployeeIn):
    print(payload, payload.dict())
    employee = await Employee.objects.acreate(**payload.dict())
    # so we don't get an error about the id
    return {"id": employee.pk}


@api.get("/employees/{employee_id}", response=EmployeeOut)
async def get_employee(request, employee_id: int):
    employee = await aget_object_or_404(Employee, pk=employee_id)
    # simply were able to return ORM object without need to convert to a dict because the resp schema does automatic result validation and JSON conversion
    return employee


@api.get("/employees", response=List[EmployeeOut])
async def list_employees(request):
    results = []
    async for employee in Employee.objects.all():
        results.append(employee)
    # simply were able to return ORM object without need to convert to a dict because the resp schema does automatic result validation and JSON conversion
    return results


@api.get("/employees-sync", response=List[EmployeeOut])
def list_employees_sycn(request):
    results = []
    for employee in Employee.objects.all():
        results.append(employee)
    # simply were able to return ORM object without need to convert to a dict because the resp schema does automatic result validation and JSON conversion
    return results


@api.put("/employees/{employee_id}")
async def update_employee(request, employee_id: int, payload: EmployeeIn):
    employee = await aget_object_or_404(Employee, pk=employee_id)
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(employee, key, value)
    await employee.asave()
    return {"success": True}


@api.delete("/employees/{employee_id}")
async def delete_employee(request, employee_id: int):
    employee = await aget_object_or_404(Employee, pk=employee_id)
    await employee.adelete()
    return {"success": True}


@api.get("/say-after")
async def say_after(request, delay: int, word: str):
    await asyncio.sleep(delay)
    return {"saying": word}
