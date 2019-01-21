
from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        # return to group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_group(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.group_name)
        self.change_field("group_header", group.group_header)
        self.change_field("group_footer", group.group_footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group fields
        self.fill_group(group)
        # submit group data
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cash = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #delete group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cash = None

    def select_group_by_index(self, index):
        # select first group
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_group(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # modify group
        wd.find_element_by_name("edit").click()
        self.fill_group(group)
        # submit group data
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        wd.find_element_by_id("logo").click()
        self.group_cash = None

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        if wd.current_url.endswith("/group.phd") and len(wd.find_elements_by_name("new"))>0:
            return
        wd.find_element_by_link_text("groups").click()


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cash = None

    def get_group_list(self):
        if self.group_cash is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cash = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cash.append(Group(group_name=text, group_id=id))
        return list(self.group_cash)




