# # from django.views.decorators.csrf import csrf_exempt
# # from django.http import HttpResponse

# # # Create your views here.

# # @csrf_exempt
# # def index(request):
# #     if request.method == 'POST':
# #         session_id = request.POST.get('sessionId')
# #         service_code = request.POST.get('serviceCode')
# #         # phone_number = request.POST.get('phonenumber')
# #         text = request.POST.get('text')

# #         response = ""

# #         if text == "":
# #             response = "END Welcome to QuickSoma,Thankyou for subscribing to a daily revision with us,we will send you questions in your inbox shortly.\n"
            
            
            
# #         # elif text =='':
# #         #         response = "END Welcome to QuickSoma,sending a text message shortly\n"


            
# #         # elif text == "":
# #         #     response = "END Welcome to QuickSoma,sending a text message shortly\n"
            
# #         return HttpResponse(response)
    
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse

# #i imported the SMS view so as to use the send function
# import sms.views as sms

# # Create your views here.

# @csrf_exempt
# def index(request):
#     if request.method == 'POST':
#         session_id = request.POST.get('sessionId')
#         service_code = request.POST.get('serviceCode')
#         phone_number = request.POST.get('phonenumber')
#         text = request.POST.get('text')

#         response = ""

#         #  I also altered this from an empty string to Nonee Value
#         if text == None:
#             response = "END Welcome to QuickSoma,Thankyou for subscribing to a daily revision with us,we will send you questions in your inbox shortly.\n"
#             #here is where you should insert the sms module to enabake start the engagement.
#             sms.send('request')
            
            
            
#         # elif text =='':
#         #         response = "END Welcome to QuickSoma,sending a text message shortly\n"


            
#         # elif text == "":
#         #     response = "END Welcome to QuickSoma,sending a text message shortly\n"
            
#         return HttpResponse(response)
    
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse

# #i imported the SMS view so as to use the send function
# import sms.views as sms

# # Create your views here.

# @csrf_exempt
# def index(request):
#     if request.method == 'POST':
#         session_id = request.POST.get('sessionId')
#         service_code = request.POST.get('serviceCode')
#         phone_number = request.POST.get('phonenumber')
#         text = request.POST.get('text')

#         response = ""

#         #  I also altered this from an empty string to Nonee Value
#         if text == None:
#             response = "END Welcome to QuickSoma,Thankyou for subscribing to a daily revision with us,we will send you questions in your inbox shortly.\n"
#             #here is where you should insert the sms module to enabake start the engagement.
#             sms.send('request')
            
            
#         return HttpResponse(response)

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
            response = "END Welcome to QuickSoma,Thankyou for subscribing to a daily revision with us,sending you an sms shortly.\n"
            
        return HttpResponse(response)