from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.



@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        admission_number = request.POST.get('admissionnumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to QuickSoma. Enter your admission\n"
            # response .= "1. My Account \n"
            response += "1. My Admission Number"

        elif text == "1":
            response = "END My Admission number is {0}".format(admission_number)
            
        return HttpResponse(response)
    return HttpResponse({"message": "this method requires a POST request"})