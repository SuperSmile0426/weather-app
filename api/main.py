from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from src.locations.router import router as locations_router
from src.forecast.router import router as forecast_router
from src.config import app_configs
from src.database import Base, engine
from src.models import Location

print("Creating database ....")

Base.metadata.create_all(engine)

app = FastAPI(**app_configs)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    print(exc)
    return JSONResponse(
        content={
            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "error_code": "validation_error",
            "message": "Request validation error",
            "detail": str(exc),
        }
    )

# Routers
app.include_router(locations_router, prefix="/locations")
app.include_router(forecast_router, prefix="/forecast")