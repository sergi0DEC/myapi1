from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models, schemas

# Crea las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()


# ---------------------------
# USUARIOS
# ---------------------------

#Crear usuario
@app.post("/usuarios/", response_model=schemas.UsuarioOut)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):

    existe = db.query(models.Usuario).filter(models.Usuario.correo == usuario.correo).first()
    if existe:
        raise HTTPException(status_code=400, detail="El correo ya está registrado.")

    nuevo = models.Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        password=usuario.password
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Listar usuarios
@app.get("/usuarios/", response_model=list[schemas.UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

# Obtener usuario por ID
@app.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioOut)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not user:
        raise HTTPException(404, "Usuario no encontrado")
    return user


# ---------------------------
# GASTOS
# ---------------------------

# Crear gasto
@app.post("/usuarios/{usuario_id}/gastos/", response_model=schemas.GastoOut)
def crear_gasto(usuario_id: int, gasto: schemas.GastoCreate, db: Session = Depends(get_db)):
    user = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not user:
        raise HTTPException(404, "Usuario no encontrado")

    nuevo = models.Gasto(
        usuario_id=usuario_id,
        **gasto.dict()
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Listar gastos de un usuario
@app.get("/usuarios/{usuario_id}/gastos/", response_model=list[schemas.GastoOut])
def listar_gastos(usuario_id: int, db: Session = Depends(get_db)):
    return db.query(models.Gasto).filter(models.Gasto.usuario_id == usuario_id).all()



