from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phonenumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "END Welcome to QuickSoma,sending a text message shortly\n"
            
            
            
        # elif text =='':
        #         response = "END Welcome to QuickSoma,sending a text message shortly\n"


            
        # elif text == "":
        #     response = "END Welcome to QuickSoma,sending a text message shortly\n"
            
        return HttpResponse(response)
    
