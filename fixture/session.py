
class SessionHelper:

    def __init__(self, app):
        self.app = app

    session = None

    def login(self, username, password):
        global session
        wd = self.app.wd
        if self.session is None:
            self.app.open_home_page()
            wd.find_element_by_id("UserName").clear()
            wd.find_element_by_name("UserName").send_keys("%s" % username)
            wd.find_element_by_name("Password").click()
            wd.find_element_by_name("Password").clear()
            wd.find_element_by_name("Password").send_keys("%s" % password)
            wd.find_element_by_xpath("//form[@class='form form-login']//button[@class='btn btn-primary']").click()
        else:
            if not fixture.application.is_session_valid():
                wd = self.app.wd
                self.app.open_home_page()
                wd.find_element_by_id("UserName").clear()
                wd.find_element_by_name("UserName").send_keys("%s" % username)
                wd.find_element_by_name("Password").click()
                wd.find_element_by_name("Password").clear()
                wd.find_element_by_name("Password").send_keys("%s" % password)
                wd.find_element_by_xpath("//button[@text='Войти']").click()


    def logout(self):
        # logout
        global session
        wd = self.app.wd
        if self.session is None:
            return
        wd.find_element_by_xpath("//form[@id='logoutFormlogout']//action").click()
