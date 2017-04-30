# -*- coding: utf-8 -*-
import pytest


from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("John", "Mark", "Smith", "Mike", "Dr", "adada", "Street", "500055555", "666666666",
                                "777777777", "11111111111", "sadadas@sadaa.com", "sadadas2@sadaa.com",
                                "sadadas3@sadaa.com", "www.home.pl", "1999", "2000", "Street2", "Home", "Bye"))
    app.session.logout()