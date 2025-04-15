from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# Base de datos SQLAlchemy
Base = declarative_base()




#### solo tablas para la base de datos ####