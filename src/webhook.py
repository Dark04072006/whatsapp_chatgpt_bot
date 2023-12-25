import logging
from typing import Any, Annotated, Callable, Awaitable

import uvicorn
from fastapi import FastAPI, Body, HTTPException
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from bot.core.settings import ALLOWED_ORIGINS, SECRET_APP_KEY
from bot.core.whatsapp_bot import whatsapp_bot

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    swagger_ui_oauth2_redirect_url=None,
)


@app.middleware("http")
async def validate_ip(
        request: Request, call_next: Callable[[Request], Awaitable[Any]]
) -> Any:
    ip = request.client.host

    if ip not in ALLOWED_ORIGINS:
        data = {"message": f"IP {ip} is not allowed to access this resource."}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=data)

    return await call_next(request)


@app.middleware("http")
async def check_auth_credentials(
        request: Request, call_next: Callable[[Request], Awaitable[Any]]
) -> Any:
    if "Authorization" not in request.headers:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    elif not request.headers["Authorization"].startswith("Bearer"):
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    token = request.headers["Authorization"].strip("Bearer ")

    if token != SECRET_APP_KEY:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    return await call_next(request)


@app.post("/webhook")
def webhook_route(event: Annotated[dict[str, Any], Body(...)]) -> None:
    try:
        whatsapp_bot.router.route_event(event)

    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=8000,
    )
