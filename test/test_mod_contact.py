

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact("John1", "Mark1", "Smith1", "Mike1", "Dr1", "adada1", "Street1", "5000555551", "6666666661",
                "7777777771", "111111111112", "sadadas1@sadaa.com", "sadadas12@sadaa.com",
                "sadadas13@sadaa.com", "www.home1.pl", "1999", "2000", "Street12", "Home1", "Bye1"))
    app.session.logout()

