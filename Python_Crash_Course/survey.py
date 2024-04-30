class AnonymousSurvey:
    
    """collect anonymous responses to a survey question"""
    
    def __init__(self, question):
        """prepare a question and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the survey question"""
        print(self.question)
        
    def store_response(self, new_response):
        """store a single response to the survey"""
        self.responses.append(new_response)
        
    def show_results(self):
        print('Survey results:\n')
        for response in self.responses:
            print(f" - {response}")
