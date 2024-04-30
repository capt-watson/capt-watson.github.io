
from exercise import Employee
import pytest

@pytest.fixture
def employee():
    """An Employee object that will be available to all test functions."""
    employee = Employee('john', 'mcKinley', 65000)
    return employee

def test_give_default_raise(employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.salary == 70000
    
def test_give_custom_raise(employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10000)
    assert employee.salary == 75000

