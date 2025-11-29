#Schema = cómo se muestra la información (validación y serialización)
from datetime import date, datetime
from pydantic import BaseModel


# ---------------------------
# USUARIO
# ---------------------------

class UsuarioBase(BaseModel):
    nombre: str
    correo: str


class UsuarioCreate(UsuarioBase):
    password: str


class UsuarioOut(UsuarioBase):
    id: int
    creado_en: datetime

    class Config:
        from_attributes = True


# ---------------------------
# GASTO
# ---------------------------
class GastoBase(BaseModel):
    categoria: str
    subcategoria: str | None = None
    descripcion: str | None = None
    monto: float
    fecha: date


class GastoCreate(GastoBase):
    pass


class GastoOut(GastoBase):
    id: int
    usuario_id: int
    creado_en: datetime

    class Config:
        from_attributes = True


# ---------------------------
# EXPORT LOG
# ---------------------------
class ExportLogOut(BaseModel):
    id: int
    archivo: str
    correo_destino: str
    fecha_envio: datetime
    mes_exportado: str

    class Config:
        from_attributes = True

