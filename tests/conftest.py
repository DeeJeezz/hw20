from unittest import mock
from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture
def director_dao():
    dao = DirectorDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def director_service(director_dao):
    return DirectorService(dao=director_dao)
