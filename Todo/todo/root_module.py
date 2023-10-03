from ellar.common import Module, exception_handler, IExecutionContext, JSONResponse, Response
from ellar.core import ModuleBase
from ellar.samples.modules import HomeModule
from .routine.module import RoutineModule


@Module(modules=[HomeModule, RoutineModule])
class ApplicationModule(ModuleBase):
    @exception_handler(404)
    def exception_404_handler(cls, ctx: IExecutionContext, exc: Exception) -> Response:
        return JSONResponse(dict(detail="Resource not found."))