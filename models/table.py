from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime
from sqlalchemy import (
    Column,
    String,
    DateTime,
)

Base = declarative_base()

# Create Table
class FilesTable(Base):
    __tablename__ = "files"
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.now)