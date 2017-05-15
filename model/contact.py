from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None, byear=None, ayear=None, address2=None, phone2=None, notes=None, id_contact=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id_contact = id_contact

    def __eq__(self, other):
        return (self.id_contact is not None or other.id_contact is not None or self.id_contact == other.id_contact) and self.firstname == other.firstname and self.lastname == other.lastname

    def __repr__(self):
        return "%s,%s,%s" % (self.id_contact, self.firstname, self.lastname)

    def id_or_max_contact(co):
        if co.id_contact is not None:
            return int(co.id_contact)
        else:
            return maxsize

