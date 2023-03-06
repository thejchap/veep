# __pragma__("skip")
import inspect
from typing import Callable

from veep import util

# pylint:disable=invalid-name
window = Vue = VueRouter = 0


ref = util.identity
create_app = util.identity


# __pragma__("noskip")

# __pragma__("ecom")
"""?
create_app = Vue.createApp
ref = Vue.ref
?"""
# __pragma__("noecom")


class VeepClient:
    def render(self):
        router = VueRouter.createRouter(
            {
                "history": VueRouter.createWebHistory(),
                "routes": self.routes,
            }
        )
        template = "<router-view />"
        props = {"template": template}
        app = Vue.createApp(props)
        app.use(router)
        app.mount("#veep")

    def __init__(self):
        self.routes = []
        # __pragma__("skip")
        self.filename = inspect.stack()[2].filename.split("/")[-1].rstrip(".py") + ".js"
        # __pragma__("noskip")

    def route(self, path: str, template: str):
        def decorator(setup: Callable):
            self._add_route(path, template, setup)
            return setup

        return decorator

    def _add_route(self, path: str, template: str, setup: Callable):
        self.routes.append(
            {
                "path": path,
                "component": {
                    "template": template,
                    "setup": setup,
                },
            }
        )
