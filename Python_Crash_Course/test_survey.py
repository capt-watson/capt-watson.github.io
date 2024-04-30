from survey import AnonymousSurvey

def test_store_five_responses():
    """Test that five individual responses are stored properly"""
    question = "Which language did you first learn to speak?\n"
    
    language_survey = AnonymousSurvey(question)
    
    responses = ['English', 'Hindi', 'Marathi', 'Gujrati', 'Spanish']
 
    for response in responses:
        language_survey.store_response(response)
        
    
    assert response in language_survey.responses
    
    #! Above test will verify that the response will end up in the survey's list of responses.
