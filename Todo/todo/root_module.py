from ellar.common import Module, exception_handler, IExecutionContext, JSONResponse, Response, IApplicationStartup
from ellar.core import ModuleBase, App
from ellar.samples.modules import HomeModule
from .routine.module import RoutineModule
from .user.module import UserModule

from .db.database import engine
from .db.models import Base


@Module(modules=[HomeModule, RoutineModule, UserModule])
class ApplicationModule(ModuleBase, IApplicationStartup):
    async def on_startup(self, app: App) -> None:
        Base.metadata.create_all(bind=engine(app.config))

    @exception_handler(404)
    def exception_404_handler(cls, ctx: IExecutionContext, exc: Exception) -> Response:
        return JSONResponse(dict(detail="Resource not found."))
