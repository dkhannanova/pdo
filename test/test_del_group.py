from model.group import Group
from random import randrange

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test_name"))
    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    app.group.delete_group_by_index(index)
    assert len(old_group) - 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group[index:index+1] = []
    assert old_group == new_group
