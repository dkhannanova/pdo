from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="1", middlename="middlename", lastname="lastname", nickname="nickname",
                    photo="C:\\Users\hannanovadm\Pictures\9908383.pdf", title="title",
                    company="company", address="address", home="home", mobile="mobile", work="work", fax="fax",
                    email="email",
                    homepage="homepage", bday="1", bmonth="August", byear="1985", address2="address2", phone="phone2",
                    notes="notes")
    contact1 = Contact(firstname="aaaa", lastname="qqqq")
    index = randrange(len(old_contact))
    if app.contact.count() == 0:
        app.contact.create_new_contact(contact)
    contact1.conid = old_contact[index].conid
    app.contact.modify_contact(contact1,index)
    old_contact[index] = contact1
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

