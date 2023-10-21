"""
@Module(
    controllers=[MyController],
    providers=[
        YourService,
        ProviderConfig(IService, use_class=AService),
        ProviderConfig(IFoo, use_value=FooService()),
    ],
    routers=(routerA, routerB)
    statics='statics',
    template='template_folder',
    # base_directory -> default is the `routine` folder
)
class MyModule(ModuleBase):
    def register_providers(self, container: Container) -> None:
        # for more complicated provider registrations
        pass

"""
from ellar.common import Module
from ellar.core import ModuleBase
from ellar.di import Container

from .controllers import RoutineController
from ..user.controllers import UserController
from .services import RoutineDB
from ..user.services import UserService


@Module(
    controllers=[RoutineController, UserController],
    providers=[RoutineDB, UserService],
    routers=[],
)
class RoutineModule(ModuleBase):
    """
    Routine Module
    """
    def register_providers(self, container: Container) -> None:
        """for more complicated provider registrations, use container.register_instance(...) """
        pass

class userModule(ModuleBase):
    def register_providers(self, container: Container) -> None:
        pass