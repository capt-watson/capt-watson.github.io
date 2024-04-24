import pytest
from survey import AnonymousSurvey

#! We need to import pytest because we are using a decorator that's defined in pytest.

@pytest.fixture
#% We apply decorator @pytest.fixture to the new function language_survey.

def language_survey():
    """A survey that will be available to all test functions"""
    #! This function builds an AnonymousSurvey object and returns the new survey.
    question = "Which language did you first learn to speak?\n"
    
    language_survey = AnonymousSurvey(question)
    
    return language_survey



#% When a parameter in a test function, matches the name a the function with @pytest.fixture decorator, the 'fixture' will run automatically and the return value will be passed to the test function.

#% In this example, the function language_survey supplies both test_store_single_response() and test_store_five_responses() with a language_survey instance.



def test_store_single_response(language_survey):
    """Test that a single response is stored properly"""
    language_survey.store_response('English')
    
    assert 'English' in language_survey.responses


    
def test_store_five_responses(language_survey):
    """Test that five individual responses are stored properly"""
    
    responses = ['English', 'Hindi', 'Marathi', 'Gujrati', 'Spanish']
    
    for response in responses:
        language_survey.store_response(response)
        
    for response in responses:
        assert response in language_survey.responses
        
#* Note that the two lines have been removed from both the above functions, as both these have been defined in the decorator function above. This fixture decorator avoids repetition of codes.

#* 1 - The line that defined question
#* 2 - The line that created an AnonymousSurvey object.

