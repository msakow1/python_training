# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


    #Testing method
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="sadaa", header="dasdada", footer="fasdada"))
    app.logout()
