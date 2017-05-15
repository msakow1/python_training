# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_group(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="sadaa", header="dasdada", footer="fasdada")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_groups_list()
    old_groups[0] = group

    assert len(old_groups) == len(new_groups)

    assert old_groups == new_groups
