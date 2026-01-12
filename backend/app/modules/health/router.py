from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def health_check():
    status = {
        "status": "OK",
        "DB": True,
        "Cache": True
    }
    return JSONResponse(content=status)