
from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

app = FastAPI()
# get_db()          abre y cierra una conexión de base de datos de forma segura.
#
# Depends(get_db)   le dice a FastAPI que esa función necesita acceso a la base de datos.
#
# read_all()        usa esa conexión para devolver todos los registros.
#
# Annotated[...]    es una forma moderna y limpia de tipar dependencias.

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
