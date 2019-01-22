from sys import maxsize
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None,
              mobile=None, email=None, snils=None, inn=None, sendsms=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.mobile = mobile
        self.email = email
        self.snils = snils
        self.inn = inn
        self.sendsms = sendsms

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.firstname, self.middlename, self.lastname, self.mobile,
                                            self.email, self.email, self.snils, self.inn, self.sendsms)

    #def __eq__(self, other):
     #   return (self.conid is None or other.conid is None or self.conid == other.conid) and self.lastname == other.lastname and self.firstname == other.firstname

    #def id_or_max(self):
     #   if self.conid:
      #      return int(self.conid)
       # else:
        #    return maxsize



