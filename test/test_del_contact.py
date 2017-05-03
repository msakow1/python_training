from model.contact import Contact


def test_add_contact(app):

    if app.contact.count() == 0:
        app.contact.create(Contact("John", "Mark", "Smith", "Mike", "Dr", "adada", "Street", "500055555", "666666666",
                                   "777777777", "11111111111", "sadadas@sadaa.com", "sadadas2@sadaa.com",
                                   "sadadas3@sadaa.com", "www.home.pl", "1999", "2000", "Street2", "Home", "Bye"))
    app.contact.delete_first()