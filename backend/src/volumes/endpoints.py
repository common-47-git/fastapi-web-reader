from fastapi import APIRouter, status
from sqlalchemy.exc import IntegrityError

from backend.src import crud, status_codes
from backend.src.database import async_session_dependency
from backend.src.volumes import schemas as volumes_schemas
from backend.src.volumes.models import VolumesModel

router = APIRouter(prefix="/volumes", tags=["volumes"])


@router.post(
    "/add",
    response_model=volumes_schemas.VolumeCreate,
    status_code=status.HTTP_201_CREATED,
)
async def volumes_add(
    session: async_session_dependency, volume: volumes_schemas.VolumeCreate,
):
    try:
        entity = await crud.create_entity(
            alchemy_model=VolumesModel, pydantic_schema=volume, session=session,
        )
        return entity
    except IntegrityError as e:
        raise status_codes.Conflict_409(exception=e)
