import pytest

from class_model import Person


class TestPerson:
    @pytest.fixture
    def setUp(self):
        self.person1 = Person("amir", "amiri")
        self.person2 = Person("ali", "alibaba")

    def test_full_name(self):
        assert self.person1.full_name() == "amir amiri"
        assert self.person2.full_name() == "ali alibaba"

    def test_email(self):
        assert self.person1.email() == "amiramiri@gmail.com"
        assert self.person2.email() == "alialibaba@gmail.com"
