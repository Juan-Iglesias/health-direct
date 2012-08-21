# Create your views here.
from health_direct.apps.inputs.checkups.AnswerApp.QuestionBuilder.models import Questions, Question_Responses

def display(id, database='answerapp'):
    question = Questions.objects.using(database).get(pk=id)
    responses = Question_Responses.objects.using(database).filter(question=question)
    
    #Placing the QuerySet in var responses into a list with unicode objects(the responses)
    rlist = []
    for response in responses:
        rlist.append(response.disp())

    # return (question.__unicode__(), rlist)
    
    # 'answerapp.html' now lies in /health_direct/apps/inputs/checkups/AnswerApp/templates/answerapp.html
    # This is a TEMPORARY solution until we discover how to nest apps in subdirectories
    
    return {'AppName': 'AnswerApp', 'Question': question, 'question_responses': rlist}