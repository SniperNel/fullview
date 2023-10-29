import asyncio
import os

import pytest
from ellar.common.constants import ELLAR_CONFIG_MODULE
from ellar.core import App
from ellar.testing import Test
from ellar.testing.module import TestingModule
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine

from .db.models import Base, User
from .db.database import get_engine, get_session_maker
from .root_module import ApplicationModule

os.environ.setdefault(ELLAR_CONFIG_MODULE, "todo.config:TestingConfig")


@pytest.fixture(scope="session")
def test_module() -> TestingModule:
    return Test.create_test_module(modules=[ApplicationModule])


@pytest.fixture(scope="session")
def app(test_module: TestingModule) -> App:
    return test_module.create_application()


@pytest.fixture(scope="session")
def client(app: App) -> AsyncClient:  # type: ignore[misc]
    with AsyncClient(app=app, base_url="http://testserver.com") as ac:
        yield ac


@pytest.fixture(autouse=True, scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def _db_engine(app):
    engine = get_engine(app.config)
    Base.metadata.create_all(bind=engine)
    print("anything")
    yield
    # print("drop all")
    # Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def db(app, _db_engine):
    """yields a SQLAlchemy connection which is rollback after the test"""
    yield app.config

# @pytest.fixture()
# def user_create(app):
#     session = SessionLocal()
#     user_details = {
#         "email":"email",
#         "first_name": "first_name",
#         "last_name": "last_name",
#         "is_active": True,
#     }
#     user = User(**user_details)
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#
#     yield user
#     session.query(User).filter(User.id == user.id).delete()
#     session.commit()