import uuid

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database import BaseAlchemyModel


class AuthorsModel(BaseAlchemyModel):
    __tablename__ = "authors"

    author_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )

    author_name: Mapped[str] = mapped_column(String(50), nullable=True)
    author_surname: Mapped[str] = mapped_column(String(50), nullable=True)

    author_books: Mapped[list["BooksModel"]] = relationship(
        back_populates="book_authors",
        secondary="books_authors",
    )

    __table_args__ = (
        UniqueConstraint(
            "author_name",
            "author_surname",
            name="uq_author_name_author_surname",
        ),
    )
