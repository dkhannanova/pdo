from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="1", middlename="middlename", lastname="lastname", nickname="nickname",
                    photo="C:\\Users\hannanovadm\Pictures\9908383.pdf", title="title",
                    company="company", address="address", home="home", mobile="mobile", work="work", fax="fax",
                    email="email",
                    homepage="homepage", bday="1", bmonth="August", byear="1985", address2="address2", phone="phone2",
                    notes="notes"))
    app.contact.modify_contact(Contact(firstname="modified1!"))
