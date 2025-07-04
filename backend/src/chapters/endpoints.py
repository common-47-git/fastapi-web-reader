from typing import Annotated

from fastapi import APIRouter, Depends, status

from backend.src.chapters import schemas as chapters_schemas
from backend.src.chapters.deps import ChaptersDeps
from backend.src.chapters.models import ChaptersModel
from backend.src.chapters.services import ChaptersServices
from backend.src.enums import ModulesEnum

router = APIRouter(
    prefix=f"/{ModulesEnum.CHAPTERS.value}",
    tags=[ModulesEnum.CHAPTERS],
)


@router.post(
    "/add",
    response_model=chapters_schemas.ChapterRead,
    status_code=status.HTTP_201_CREATED,
    summary="Add a chapter to a volume.",
)
async def chapters_add(
    chapter: chapters_schemas.ChapterCreate,
):
    """Add a chapter to an existing volume linked by volume_id."""
    return await ChaptersServices().create_one(pydantic_schema=chapter)


@router.get(
    "/read/{book_name}",
    response_model=chapters_schemas.ChapterRead,
    summary="Read a chapter.",
)
async def books_get_read_by_name(
    book_name: str,
    volume_number: int = 1,
    chapter_number: int = 1,
):
    """Read a chapter linked with book by volume_id and book_id."""
    return await ChaptersServices().read_book_chapter(
        book_name=book_name,
        volume_number=volume_number,
        chapter_number=chapter_number,
    )


@router.delete(
    "/{chapter_id}",
    response_model=chapters_schemas.ChapterRead,
    summary="Delete a chapter.",
)
async def chapters_delete_by_id(
    existing_chapter: Annotated[
        ChaptersModel,
        Depends(ChaptersDeps.one_exists),
    ],
):
    """Delete a chapter by id."""
    return await ChaptersServices().delete_one(
        alchemy_object=existing_chapter,
    )
