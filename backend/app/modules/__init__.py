from fastapi import FastAPI

def register_modules(app: FastAPI, common_prefix: str = "/api"):
    from .auth import router as auth_router
    from .event import router as event_router
    from .analytics import router as analytics_router
    from .notify import router as notify_router
    from .health import router as health_router

    app.include_router(auth_router, prefix=f"{common_prefix}/auth", tags=['auth'])
    app.include_router(event_router, prefix=f"{common_prefix}/events", tags=['events'])
    app.include_router(analytics_router, prefix=f"{common_prefix}/analytics", tags=['analytics'])
    app.include_router(notify_router, prefix=f"{common_prefix}/notify", tags=['notify'])
    app.include_router(health_router, prefix=f"{common_prefix}/health", tags=['health'])