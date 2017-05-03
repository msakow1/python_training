# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="sadaa", header="dasdada", footer="fasdada"))
    app.group.modify_first_group(Group(name="sad1"))
