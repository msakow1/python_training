from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact("John", "Mark", "Smith", "Mike", "Dr", "adada", "Street", "500055555", "666666666",
                                   "777777777", "11111111111", "sadadas@sadaa.com", "sadadas2@sadaa.com",
                                   "sadadas3@sadaa.com", "www.home.pl", "1999", "2000", "Street2", "Home", "Bye"))
    app.contact.delete_first()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)

    assert old_contact[1:len(old_contact)] == new_contact