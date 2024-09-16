import uvicorn
from fastapi import FastAPI


from api import router
from config import settings

main_app = FastAPI(
    title="IT Solutions Service API",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
)

main_app.include_router(router=router, prefix=settings.api.prefix)

if __name__ == '__main__':
    uvicorn.run(
        "main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )