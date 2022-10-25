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
         
            
#         return HttpResponse(response)
#     return HttpResponse({"message": "this method requires a POST request"})

# import self from
import africastalking
class SMS:
    def __init__(self):
        self.username = "upeo"
        self.api_key = "8aa33b77936ad87e942ebb4aba80175f2a87a4b0c94fefb44e4ab086c07c570d"
        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
        # Get the SMS service
        self.sms = africastalking.SMS
    def send(self):
        recipients = ["+256787955445"]
        # Set your message
        message = "Hello Learner, Welcome to QuickSoma. Enter your phone number";
        # Set your shortCode or senderId
        # sender = "4632"
        try:
            response = self.sms.send(message, recipients)
            print (response)
        except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))
if __name__ == '__main__':
     SMS().send()
