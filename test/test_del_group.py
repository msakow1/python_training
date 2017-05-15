from model.group import Group

def test_del_group(app):
    old_groups = app.group.get_groups_list()
    group = old_groups[0].id
    app.group.delete_first_group()
    new_groups = app.group.get_groups_list()
#    old_groups[0] = []

    assert len(old_groups)-1 == len(new_groups)

    assert old_groups[1:len(old_groups)] == new_groups