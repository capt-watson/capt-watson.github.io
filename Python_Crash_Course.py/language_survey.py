from survey import AnonymousSurvey

question = "Which language did you first learn to speak?\n"

language_survey = AnonymousSurvey(question)  ## language_survey is an instance of AnonymousSurvey class.

language_survey.show_question()

print("Enter 'q' anytime to quit,\n")

while True:
    response = input("Enter language: ")    ## Accepting user response
    
    if response == "q":
        break
    
    language_survey.store_response(response)
    
print("A big thanks to everyone who participated in the survey!\n")

language_survey.show_results()
