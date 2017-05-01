# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="sadaa", header="dasdada", footer="fasdada"))
    app.group.delete_first_group()
    app.group.modify_first_group(Group(name="sad0", header="dasd0", footer="fasd0"))
    app.session.logout()