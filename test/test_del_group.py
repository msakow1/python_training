from model.group import Group

def test_del_group(app):
    app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="sadaa", header="dasdada", footer="fasdada"))
    app.group.delete_first_group()
    app.session.logout()