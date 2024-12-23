from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.routes.hello import router as hello_router
from src.api.router import router
from src.api.routes.data import router as data_router



def get_application() -> FastAPI:
    application = FastAPI(
        title="epf-flower-data-science",
        description="""Fast API""",
        version="1.0.0",
        redoc_url=None,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router)
    application.include_router(hello_router, tags=["Demo"])
    application.include_router(data_router, tags=["Data"])
    return application
