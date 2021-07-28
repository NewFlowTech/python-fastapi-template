from fastapi import FastAPI
from core.settings import cfg
from fastapi.middleware import (
    cors,
    trustedhost
)
from fastapi.openapi.utils import get_openapi
from domain.routers.health import api as health_router

app = FastAPI(
    title=cfg.app_name.value,
    debug=cfg.app_debug.value
)

app.include_router(health_router)

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    trustedhost.TrustedHostMiddleware,
    allowed_hosts=cfg.app_allowed_hosts.value
)

def custom_openapi():
    openapi_schema = get_openapi(
        title=f"{cfg.app_name.value} - DOCUMENTATION",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    from core.settings import cfg
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=cfg.app_port.value if cfg.app_port.value else 4000,
        reload=True
    )

