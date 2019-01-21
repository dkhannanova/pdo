import re
from random import randrange

def test_home_page_table(app):
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = contact_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.allphones_from_home_page == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.email == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                              filter(lambda x: x is not None,
                                                     [contact.home, contact.mobile, contact.work, contact.phone]))))
def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0),
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone == contact_from_edit_page.phone

def clear(s):
    return re.sub("[()-]", "", s)