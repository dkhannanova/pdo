
class SessionHelper:

    def __init__(self, app):
        self.app = app

    session = None

    def login(self, username, password):
        global session
        wd = self.app.wd
        if self.session is None:
            self.app.open_home_page()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys("%s" % username)
            wd.find_element_by_name("pass").click()
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys("%s" % password)
            wd.find_element_by_xpath("//input[@value='Login']").click()
        else:
            if not fixture.application.is_session_valid():
                wd = self.app.wd
                self.app.open_home_page()
                wd.find_element_by_name("user").clear()
                wd.find_element_by_name("user").send_keys("%s" % username)
                wd.find_element_by_name("pass").click()
                wd.find_element_by_name("pass").clear()
                wd.find_element_by_name("pass").send_keys("%s" % password)
                wd.find_element_by_xpath("//input[@value='Login']").click()




    def logout(self):
        # logout
        global session
        wd = self.app.wd
        if self.session is None:
            return
        wd.find_element_by_name("logout").click()
