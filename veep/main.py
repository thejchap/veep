# __pragma__("skip")

import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.types import Receive, Scope, Send

# __pragma__("noskip")


# pylint:disable=pointless-string-statement
"""
keep export outside of skip
"""
# pylint:disable=wrong-import-position
from veep import util
from veep.client import VeepClient

# __pragma__("skip")


class VeepAPI(FastAPI):
    ...


class VeepServer(FastAPI):
    ...


# __pragma__("noskip")


class VeepServerStub:
    get = post = put = delete = patch = util.decorator_identity


class Veep:
    def __init__(self, title: str = "Veep"):
        self.client = VeepClient()
        # __pragma__("ecom")
        """?
        self.server = VeepServerStub()
        ?"""
        # __pragma__("noecom")

        # __pragma__("skip")

        self.title = title
        self.server = VeepAPI(title=title)
        self._server = VeepServer(title=title)
        self._server.mount("/api", self.server)
        self._server.add_api_route(
            "/",
            self.async_index,
            methods=["GET"],
            response_class=HTMLResponse,
        )
        self._server.mount(
            "/__veep__/static",
            StaticFiles(directory="./veep/static"),
            name="static",
        )
        self._templates = Jinja2Templates(
            directory="./veep/templates",
        )
        self._server.add_event_handler("startup", self._on_startup)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        await self._server(scope, receive, send)

    async def async_index(self, req: Request):
        client_path = f"/__target__/{self.client.filename}"
        return self._templates.TemplateResponse(
            "index.html",
            context={
                "title": self.title,
                "request": req,
                "spa_path": client_path,
            },
        )

    def _on_startup(self):
        transpile_cmd = f"""\
transcrypt \
    --kwargs \
    --nomin \
    --map \
    --build \
    --outdir {os.getcwd()}/veep/static/__target__ \
    example.py"""
        os.system(transpile_cmd)


# __pragma__("noskip")
