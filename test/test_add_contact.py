# -*- coding: utf-8 -*-

from model.contact import Contact
from fixture.contact import ContactHelper

def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact("John", "Mark", "Smith", "Mike", "Dr", "adada", "Street", "500055555", "666666666",
                                "777777777", "11111111111", "sadadas@sadaa.com", "sadadas2@sadaa.com",
                                "sadadas3@sadaa.com", "www.home.pl", "1999", "2000", "Street2", "Home", "Bye")
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)

    old_contact.append(contact)

    assert sorted(old_contact, key=Contact.id_or_max_contact) == sorted(new_contact, key=Contact.id_or_max_contact)
