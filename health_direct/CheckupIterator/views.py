from health_direct.InputSubmitBackend.models import Input, Apps
import os

def get_checkup(record):
    # Looks up app_foreignkey in the record
    # Get appcode and app out of record
    a1 = Apps.objects.get(name=record.app)
    # calls program at location with the id of the particular checkup as the argument
    # Runs app within checkupiterator window.
    os.system(str(a1.location) + ' ' + str(record.app_code))
    # When the app completes running it sends the result to User_Entries table
    
def queuer(request):
    # if (request.session['member_id']) if it exists
    #     User_Input.objects.get(user=request.session['member_id'])
    #     select the most appropriate input (this will return an input primary key)
    #     of the most appropriate input, grab its app
    #     Input.objects.get(pk=selectedcheckup).answerapp
    # else
    #    display a different page, redirect to the register or login page
    