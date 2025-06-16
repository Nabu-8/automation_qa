import pytest
from lesson_16.homework_14_task_1 import *

@pytest.mark.hw14
@pytest.mark.positive
def test_teamlead_attributes():
    team_lead = TeamLead(
        name="Eric",
        salary=100,
        department="DevOps",  # Manager
        programming_language="Python",  # Developer
        team_size=3  # Own attribute
    )

    assert hasattr(team_lead, 'name'), "TeamLead should have 'name' attribute"
    assert hasattr(team_lead, 'salary'), "TeamLead should have 'salary' attribute"
    assert hasattr(team_lead, 'department'), "TeamLead should have 'department' attribute from Manager"
    assert hasattr(team_lead, 'programming_language'), "TeamLead should have 'programming_language' attribute from Developer"
    assert hasattr(team_lead, 'team_size'), "TeamLead should have his one 'team_size' attribute"

    assert team_lead.name == "Eric", "'name' attribute should be 'Eric'"
    assert team_lead.salary == 100, "'salary' attribute should be 100"
    assert team_lead.department == "DevOps", "'department' attribute should be 'DevOps'"
    assert team_lead.programming_language == "Python", "'programming_language' attribute should be 'Python'"
    assert team_lead.team_size == 3, "'team_size' attribute should be 3"


@pytest.mark.hw14
@pytest.mark.positive
def test_manager_attributes():
    manager = Manager(
        name="Katy",
        salary=80,
        department="PM" # Own attribute

    )

    assert hasattr(manager, 'name'), "Manager should have 'name' attribute"
    assert hasattr(manager, 'salary'), "Manager should have 'salary' attribute"
    assert hasattr(manager, 'department'), "Manager should have 'department' attribute"

    assert manager.name == "Katy", "'name' attribute should be 'Katy'"
    assert manager.salary == 80, "'salary' attribute should be 80"
    assert manager.department == "PM", "'department' attribute should be 'PM'"



@pytest.mark.hw14
@pytest.mark.positive
def test_developer_attributes():
    developer = Developer(
        name="Charly",
        salary=90,
        programming_language="JS" # Own attribute
    )

    assert hasattr(developer, 'name'), "Developer should have 'name' attribute"
    assert hasattr(developer, 'salary'), "Developer should have 'salary' attribute"
    assert hasattr(developer, 'programming_language'), "Developer should have 'programming_language' attribute from Developer"

    assert developer.name == "Charly", "'name' attribute should be 'Charly'"
    assert developer.salary == 90, "'salary' attribute should be 90"
    assert developer.programming_language == "JS", "'programming_language' attribute should be 'JS'"



# Solution for future via dictionary
# @pytest.mark.hw14
# @pytest.mark.positive
# def test_teamlead_attributes_2():
#     team_lead = TeamLead(name="Eric", salary=100, department="DevOps", programming_language="Python", team_size=3)
#     expected_attrs = {'name': "Eric", 'salary': 100, 'department': "DevOps", 'programming_language': "Python", 'team_size': 3}
#
#     for attr, expected_value in expected_attrs.items():
#         assert hasattr(team_lead, attr), f"{attr} is not found"
#         assert getattr(team_lead, attr) == expected_value, f"{attr} should be {expected_value}"
#
# @pytest.mark.hw14
# @pytest.mark.positive
# def test_manager_attributes_2():
#     manager = Manager(name="Katy", salary=80, department="PM")
#     expected_attrs = {'name': "Katy", 'salary': 80, 'department': "PM"}
#
#     for attr, expected_value in expected_attrs.items():
#         assert hasattr(manager, attr), f"{attr} is not found"
#         assert getattr(manager, attr) == expected_value, f"{attr} should be {expected_value}"
#
# @pytest.mark.hw14
# @pytest.mark.positive
# def test_developer_attributes_2():
#     developer = Developer(name="Charly", salary=90, programming_language="JS")
#     expected_attrs = {'name': "Charly", 'salary': 90, 'programming_language': "JS"}
#
#     for attr, expected_value in expected_attrs.items():
#         assert hasattr(developer, attr), f"{attr} is not found"
#         assert getattr(developer, attr) == expected_value, f"{attr} should be {expected_value}"