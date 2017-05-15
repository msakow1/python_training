# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="sadaa", header="dasdada", footer="fasdada")
    app.group.create(group)
    new_groups = app.group.get_groups_list()

    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


