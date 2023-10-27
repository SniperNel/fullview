import pytest
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean
from .db.database import SessionLocal, engine
#from .db.models import User


@pytest.fixture(scope="function")
def temp_dp():
    metadata = MetaData()
    users = Table(
        "uses",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("email", String),
        Column("first_name", String),
        Column("last_name", String),
        Column("is_active", Boolean, default=True),
    )

    metadata.create_all(engine)
    session = SessionLocal()

    session.add(users)
    yield session

    session.close()
    metadata.drop_all(engine)