from fastapi import FastAPI

def register_modules(app: FastAPI):
    from .auth import router as auth_router
    from .event import router as event_router
    from .analytics import router as analytics_router
    from .notify import router as notify_router

    app.include_router(auth_router, prefix='/auth', tags=['auth'])
    app.include_router(event_router, prefix='/events', tags=['events'])
    app.include_router(analytics_router, prefix='/analytics', tags=['analytics'])
    app.include_router(notify_router, prefix='/notify', tags=['notify'])