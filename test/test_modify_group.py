from model.group import Group
from random import randrange

def test_modify_group(app):
    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    group = Group(group_name="name1", group_header="header1", group_footer="footer1")
    group1 = Group(group_name="m1")
    group1.id = old_group[index].id
    group1.group_header = old_group[index].group_header
    group1.group_footer = old_group[index].group_footer
    if app.group.count() == 0:
        app.group.create(group)
    app.group.modify_group(group1, index)
    old_group[index] = group1
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)

