# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse

# # Create your views here.



# @csrf_exempt
# def index(request):
#     if request.method == 'POST':
#         session_id = request.POST.get('sessionId')
#         service_code = request.POST.get('serviceCode')
#         admission_number = request.POST.get('admissionnumber')
#         text = request.POST.get('text')

#         response = ""

#         if text == "":
#             response = "CON Welcome to QuickSoma. Enter your admission\n"
#             # response .= "1. My Account \n"
#             response += "1. My Admission Number"

#         elif text == "1":
#             response = "END My Admission number is {0}".format(admission_number)



#         elif text == "1":
#             response = "CON Get smarter in Mathematics today with QuickSoma \n"
#             response += "1. Choose topic for revision\n"
#         elif text == "1*1":
#             response = "CON  Topics\n"
#             response += "1. Area\n"
#             response += "2. Indices \n"
#         elif text == "1*1*1":
#             response = "CON  Attempt the following questions \n"
#             response += "1. What is the area of a square whose side is 6cm (Tip:Area=s*s) \n"
          
#         elif text == "1*1*1*1":
#             response += "CON 1. Choose the correct answer\n"
#         elif text == "1*1*1*1*1":
#             response = "CON Choose the type of bill you pay \n"
#             response += "1. 20cm \n"
#             response += "2. 38cm \n"
#             response += "3. 36cm^2 \n"
#             response += "4. 40cm^2 \n"
#         elif text == "1*1*1*1*1*3":
#             response = "CON Congratulations for revising with QuickSoma.The correct answer is 36cm^2.To continue revising press 0 to go back to revision questions \n"
         
            
#         return HttpResponse(response)
#     return HttpResponse({"message": "this method requires a POST request"})
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from random import randint
# from .utils *
# from .models *

# Create your views here.


@csrf_exempt
def index(request):

    if request.method == 'POST':
        # session_id = request.POST.get('sessionId')
        # service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')


        response = ""

        if text == "":
            response = "CON What would you want to check \n"
            response += "1.View Phone Number\n 2.Know my capital City\n0.Exit"
        else:

            text_string = text.split('*') # user input is in the form *384*1234*1*4*2#, split to get most recent input
            user_response = text_string[-1].strip()

            menu = randint(0, 3)


            if user_response == "1":
                response = "CON Your phone number is {0}\n00.Back\n0.Exit".format(phone_number)
            elif user_response == "2":
                response = "CON Your Capital is Nairobi\n00.Back\n0.Exit"
            elif user_response == "0":
                response = "END Goodbye!!"
            elif user_response == "00":
                response = "CON What would you want to check \n"
                response += "1.View Phone Number\n 2.Know my capital City\n3.Exit"

        return HttpResponse(response)
    return HttpResponse({"message": "this method requires a POST request"})
