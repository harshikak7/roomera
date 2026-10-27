from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base 

class Student(Base):
    __tablename__="students"

    id: Mapped[int]=mapped_column(
        Integer, primary_key=True, index=False
    )

    