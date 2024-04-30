from name_function import get_formatted_name

def test_first_last_name():     #! must save this code under separate test_ file.
    """Test the for various conditions"""
    formatted_name= get_formatted_name('John','Mckinley')  ## function needs to be tested with given attributes
    assert formatted_name == 'John Mckinley'               ## Final result should be this.
    
    #! to run this pytest, open the terminal window and enter pytest. The test will automatically run to check if the assertion is correct.
    #! if the assertion is correct, the test will pass. If the assertion is incorrect, the test will fail.
    
    
def test_first_last_middle_name():
    """test the get_formatted_name() function"""
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
