from email import message
from urllib import response
from django.http import Http404
from fastapi import APIRouter, Response, status
from sqlalchemy import null
from config.db import conn
from models.departamento import departamentos
from schemas.departamento import Departamento
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from fastapi.responses import JSONResponse


departamento = APIRouter()

@departamento.get("/departamentos", response_model=list[Departamento])
def get_departamentos():
    return conn.execute(departamentos.select()).fetchall()
 
@departamento.post("/departamentos", response_model=Departamento)
def create_departamento(departamento: Departamento):
    new_departamento = {"name":departamento.name, "ref":departamento.ref}
    result = conn.execute(departamentos.insert().values(new_departamento))
    return conn.execute(departamentos.select().where(departamentos.c.id == result.lastrowid)).first()

@departamento.get("/departamentos/{id}", response_model=Departamento)
def get_departamento(id: str):
    result = conn.execute(departamentos.select().where(departamentos.c.id == id)).first()
   
    if result is None:
        return JSONResponse(content={ "ok": True, "message": "No records found"})

    return result


@departamento.put("/departamentos/{id}", response_model=Departamento)
def update_departamento(id: str, departamento: Departamento):
    conn.execute(departamentos.update().values(name= departamento.name, ref = departamento.ref).where(departamentos.c.id == id))  
    return "update"


@departamento.delete("/departamentos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_departamento(id: str):
    return conn.execute(departamentos.delete().where(departamentos.c.id == id))
