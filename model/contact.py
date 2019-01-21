from sys import maxsize
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None,
                 nickname=None, photo=None, title=None, company=None, address=None,
                 home=None, mobile=None, work=None, fax=None, email=None, homepage=None, bday=None, bmonth=None, byear=None, address2=None, phone=None, notes=None, conid=None,
                 allphones_from_home_page=None, email2=None, email3=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
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
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.phone = phone
        self.notes = notes
        self.conid = conid
        self.allphones_from_home_page = allphones_from_home_page


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.conid, self.lastname, self.firstname, self.allphones_from_home_page, self.email, self.address)

    def __eq__(self, other):
        return (self.conid is None or other.conid is None or self.conid == other.conid) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.conid:
            return int(self.conid)
        else:
            return maxsize



