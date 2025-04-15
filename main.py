from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from models import Base 

# Configuración de la aplicación FastAPI
app = FastAPI()

# Configuración de la base de datos SQLite   --motor
DATABASE_URL = "sqlite:///./Aeropuerto.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)



#### Main para toda la gestion  #####
