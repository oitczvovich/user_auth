from fastapi import FastAPI

from .api.api import router
from user_auth.core.config import settings


app = FastAPI(title=settings.app_title)

app.include_router(router)
