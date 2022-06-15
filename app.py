from fastapi import FastAPI
from routers.departamento import departamento

app = FastAPI(
    title="Departamentos"
)

app.include_router(departamento)

