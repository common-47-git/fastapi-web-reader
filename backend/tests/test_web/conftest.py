import pytest

from backend.src.authors.schemas import AuthorInDB
from backend.src.books.schemas import BookInDB
from backend.src.enums import TranslationStatusEnum
from backend.src.tags.schemas import TagInDB
from backend.src.users.schemas.users import UserInDB


@pytest.fixture
def test_user_in_db(faker):
    return UserInDB(
        user_id=faker.uuid4(),
        username=faker.user_name(),
        email=faker.email(),
        registration_date=faker.date(),
        password=faker.password(),
    )


@pytest.fixture
def test_book_in_db(faker):
    return BookInDB(
        book_id=faker.uuid4(),
        book_name=faker.user_name(),
        book_country=faker.country(),
        book_release_date=faker.date(),
        book_translation_status=TranslationStatusEnum.ABSENT,
        book_description=faker.text(),
    )


@pytest.fixture
def test_author_in_db(faker):
    return AuthorInDB(
        author_id=faker.uuid4(),
        author_name=faker.name().split()[0],
        author_surname=faker.name().split()[1],
    )


@pytest.fixture
def test_tag_in_db(faker):
    return TagInDB(
        tag_id=faker.uuid4(),
        tag_name=faker.name(),
    )
