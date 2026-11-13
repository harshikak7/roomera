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

    student_code: Mapped[str]=mapped_column(
        String(50), unique=True, nullable=False
    )

    institutional_email: Mapped[str]=mapped_column(
        String(100), unique=True, nullable=False
    )

    full_name: Mapped[str]=mapped_column(
        String(150), nullable=False
    )

    gender:Mapped[str]=mapped_column(
        String(20), nullable=False
    )
    course: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    academic_year: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    profile: Mapped["RoomeraProfile | None"] = relationship(
        back_populates="student",
        uselist=False,
        cascade="all, delete-orphan"
    )

class RoomeraProfile(Base):
    __tablename__="roomera_profiles"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )
    bio: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )
    avatar_key: Mapped[str | None] = mapped_column(
        String(100), nullable=True
    )
    interests: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )

    student: Mapped["Student"] = relationship(
        back_populates="profile"
    )