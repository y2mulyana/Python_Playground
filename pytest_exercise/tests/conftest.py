import pytest
import source.shapes as shape

"""
Setup: Fixtures are typically used to prepare the necessary environment, such as creating objects or setting up mock data. 
       This allows tests to focus on functionality, rather than setup. 

Scope: Fixtures can have different scopes that control their lifecycle. For example:
       - 'function' scope: The fixture is invoked once per test function.
       - 'module' scope: The fixture is invoked once per module.
       - 'session' scope: The fixture is invoked once per session.
       The scope determines how frequently the fixture is created and shared across tests.

Sharing: Fixtures can be reused across multiple tests. This helps reduce redundancy and ensures consistency.

conftest.py:

Global Fixtures: You can define fixtures in conftest.py that can be used by all test files within the same directory or project.
Custom Hooks: can be used to define custom pytest hooks, which allow you to modify the behavior of pytest during the test discovery, setup, and execution process.
Configuration: It allows you to configure pytest settings globally
Plugin Integration: integrate and configure third-party pytest plugins
"""


# Fixture to create a Rectangle object with predefined dimensions: length=10, width=4
@pytest.fixture
def rec_value():
    return shape.Rectangle(length=10, width=4)


# Fixture to create a Rectangle object with different dimensions: length=8, width=7
@pytest.fixture
def rec_weird():
    return shape.Rectangle(length=8, width=7)