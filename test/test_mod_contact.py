

from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("John", "Mark", "Smith", "Mike", "Dr", "adada", "Street", "500055555", "666666666",
                                   "777777777", "11111111111", "sadadas@sadaa.com", "sadadas2@sadaa.com",
                                   "sadadas3@sadaa.com", "www.home.pl", "1999", "2000", "Street2", "Home", "Bye"))
    app.contact.modify_first(Contact("John1", "Mark1", "Smith1", "Mike1", "Dr1", "adada1", "Street1", "5000555551", "6666666661",
                "7777777771", "111111111112", "sadadas1@sadaa.com", "sadadas12@sadaa.com",
                "sadadas13@sadaa.com", "www.home1.pl", "1999", "2000", "Street12", "Home1", "Bye1"))


