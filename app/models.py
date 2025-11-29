#Model = cómo se guarda en la base de datos
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    # relación 1-N con gastos
    gastos = relationship("Gasto", back_populates="usuario")
    export_logs = relationship("ExportLog", back_populates="usuario")


class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    categoria = Column(String, nullable=False)
    subcategoria = Column(String)
    descripcion = Column(String)
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="gastos")


class ExportLog(Base):
    __tablename__ = "export_logs"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    archivo = Column(String, nullable=False)  # nombre o path del excel generado
    correo_destino = Column(String, nullable=False)
    fecha_envio = Column(DateTime, default=datetime.utcnow)
    mes_exportado = Column(String, nullable=False)  # ejemplo: "2025-02"

    usuario = relationship("Usuario")
