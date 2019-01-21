# -*- coding: utf-8 -*-
from selenium import webdriver
import string
import pytest
import random
from model.contact import Contact


def test_add_contact(app, json_contact):
    contact = json_contact
    old_contact = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contact)+1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)






