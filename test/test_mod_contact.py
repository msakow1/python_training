

from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact("John1", "Mark1", "Smith1", "Mike1", "Dr1", "adada1", "Street1", "5000555551", "6666666661",
                "7777777771", "111111111112", "sadadas1@sadaa.com", "sadadas12@sadaa.com",
                "sadadas13@sadaa.com", "www.home1.pl", "1999", "2000", "Street12", "Home1", "Bye1")
    contact.id_contact = old_contact[0].id_contact
    app.contact.modify_first(contact)
    new_contact = app.contact.get_contact_list()
    old_contact[0] = contact
    assert len(old_contact) == len(new_contact)

    assert sorted(old_contact, key=Contact.id_or_max_contact) == sorted(new_contact, key=Contact.id_or_max_contact)
