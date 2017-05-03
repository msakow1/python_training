

class GroupHelper:
    def __init__(self,app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.group_page()
        # Create new group
        wd.find_element_by_name("new").click()
        # Fill groups details
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        self.value_exists("group_name", group.name)
        self.value_exists("group_header", group.header)
        self.value_exists("group_footer", group.footer)

    def value_exists(self, field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def modify_first_group(self,group):
        wd = self.app.wd
        self.group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


    def group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook")


    def count(self):
        wd = self.app.wd
        self.group_page()
        return len(wd.find_elements_by_name("selected[]"))
