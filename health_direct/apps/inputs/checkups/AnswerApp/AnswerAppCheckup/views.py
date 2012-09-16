# Create your views here.
from health_direct.apps.inputs.checkups.AnswerApp.QuestionBuilder.models import Questions, Question_Responses

def display(ident, database='answerapp'):
    'Provides display information from checkups obtained from the AnswerApp'
    
    #Grabs the question being asked by health-direct
    question = Questions.objects.using(database).get(pk=ident)
    
    #Grabs the responses the the question being asked
    responses = Question_Responses.objects.using(database).filter(question=question)
    
    #Placing the QuerySet in variable responses into a list with unicode objects(the responses)
    rlist = []
    for response in responses:
        rlist.append(response.disp())

    return {'AppName': 'AnswerApp', 'Question': question, 'question_responses': rlist}