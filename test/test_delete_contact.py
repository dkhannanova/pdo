from model.contact import Contact
from random import randrange

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname=1))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index+1] = []
    assert new_contact == old_contact

