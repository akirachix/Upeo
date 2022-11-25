# # # import africastalking
# # # from rest_framework.response import Response 
# # # from rest_framework.decorators import api_view
# # # from django.shortcuts import render
# # # from upeoapp import models
  
# # # def send_sms(request):
# # #     username = "Sandbox"
# # #     api_key = "0ea2ef02a865ff37721386a3cec39ebe2294d40af0e4bdddae9c567f67e0fa9e"

# # #     # Initialize the SDK
# # #     africastalking.initialize(username, api_key)
# # #     # Get the SMS service
# # #     sms = africastalking.SMS
    
# # #     # recipients = "sand"
# # #     sender = "84028"

# # #     # Set your message
# # #     # message = "Hello Learner,find the area of the triangle below.";
# # #     questions=models.Questions.objects.all()
    
        
# # #     for x in range(len(questions)):
# # #             print(questions[x])
# # #     quest=questions.question
    
# # #     message=f"Hello your question is {questions[x]}"

              
# # #     # Set your shortCode or senderId
# # #     # sender = "4632"
    
# # #     try:
# # #         response = sms.send(message, sender)
        
# # #         return render(request,"test.html",{"response":response})
# # #     except Exception as e:
# # #         return render(request,"test.html",{"response":e})
    
# # # from requests import request
# # # from . import upeo
# # # import requests
# # # from rest_framework.response import Response 
# # # from rest_framework.decorators import api_view
# # # from django.shortcuts import render
# # # from upeoapp import models
# # # from . import views
# # # # from sms import app



# # # @upeo.upeoapp('/')
# # # def hello_world():
# # #         return 'Hello,Leaner'
    
# # # @upeo.upeoapp('/sms_callback',methods=['POST'])
# # # def sms_callback():
# # #     print(request.method)
# # #     print(request.form)
# # #     print(request.form("from"))
# # #     response_to_sms(request.form["from"],request.form["text"])
# # #     return "Success",201

# # # SANDBOX_API_KEY="bd94656251d9ede64d0d48351f12761f3d94dad80ace7e52032e4e2f8195eb56"

# # # def response_to_sms(recipient_phone_number,message):
# # #     requests.post(
# # #         "https://api.sandbox.africastalking.com/version1/messaging",
# # #         data={
# # #             "username": "sandbox",
# # #             "to":recipient_phone_number,
# # #             "message":message,
# # #             "from":"85828",
# # #         },
# # #         header={
# # #             "apiKey":SANDBOX_API_KEY,
# # #             "Accept":"application/json",
# # #             "Content-Type":"application/x-www-form-urlencoded"
# # #         }
# # #     )
         
# # # from datetime import datetime
# # # import africastalking
# # # import requests
# # # from upeoapp.models import Questions, Answers
# # # # Initialize SDK
# # # username = "Sandbox"
# # # api_key = "ee4e8964e4c5b662483bf5a25b6af88a393a3ad5c1ead01ac7dcfbdd511e0dd0"
# # # africastalking.initialize(username, api_key)
# # # sms = africastalking.SMS
# # # def send_sms(user,message):
# # #     """
# # #     Send sms
# # #     """
# # #     # recipients = recipients
# # #     message = "Hello your question is {questions[x]}"
# # #     time_sent = datetime.now()
# # #     #
# # #     if len(message) > 160:
# # #         raise Exception("Ensure your message has less that 160 characters")
# # #     try:
# # #         # buy a Dedicated Short Code to get a sender ID
# # #         # response = sms.send(message, recipients, sender)
# # #         response = sms.send()
# # #         # save the sms info to the db
# # #         sms_info_obj = Questions(
# # #             time_sent=time_sent,
# # #             message_text=message,
# # #             africastalking_response=response['SMSMessageData']['Message'],
# # #             user=user,
# # #             success=True)
# # #         sms_info_obj.save()
# # #         # save the messages sent
# # #         contact_list = contact_obj.objects.all()
# # #         message_obj_list = []
# # #         for i in response['SMSMessageData']['Recipients']:
# # #             # check for contact
# # #             if contact_list.filter(phone_number__exact=i["+254702632852"]).exists:
# # #                 # if we have the contact saved...
# # #                 message_obj_list.append(
# # #                     message(
# # #                         message_info=sms_info_obj,
# # #                         message_id=i["messageId"],
# # #                         contact=contact_list.get(
# # #                             phone_number__exact=i["+254702632852"]),
# # #                         cost=i["cost"],
# # #                         status_code=i["statusCode"],
# # #                         number=i["number"]
# # #                     ))
# # #             else:
# # #                 # create & save contact
# # #                 contact_obj = contact_list(
    
# # #                     phone_number=i["number"])
# # #                 contact_obj.save()
# # #                 #
# # #                 #
# # #                 # save message
# # #                 message_obj_list.append(
# # #                     message(
# # #                         message_info=sms_info_obj,
# # #                         message_id=i["messageId"],
# # #                         contact=contact_obj,
# # #                         cost=i["cost"],
# # #                         number=i["number"],
# # #                         status_code=i["statusCode"], ))
# # #         # save the list objects into the database in one query
# # #         message.objects.bulk_create(message_obj_list)
# # #     except requests.exceptions.ConnectionError as e:
# # #         # save the sms info to the db
# # #         sms_info_obj = Questions(
# # #             time_sent=time_sent,
# # #             message_text=message,
# # #             africastalking_response=e,
# # #             user=user,
# # #             success=False)
# # #         sms_info_obj.save()
# # #         raise Exception("Network Connection Error")
# # #     except requests.HTTPError as e:
# # #         # save the sms info to the db
# # #         sms_info_obj = Questions(
# # #             time_sent=time_sent,
# # #             message_text=message,
# # #             africastalking_response=e,
# # #             user=user,
# # #             success=False)
# # #         sms_info_obj.save()
# # #         raise Exception("HTTP Network Error")
# # #     except Exception as e:
# # #         # save the sms info to the db
# # #         sms_info_obj = sms(
# # #             time_sent=time_sent,
# # #             message_text=message,
# # #             africastalking_response=e,
# # #             user=user,
# # #             success=False)
# # #         sms_info_obj.save()
# # #         raise e
# # #     else:
# # #         return response


# # # import africastalking
# # # from rest_framework.response import Response 
# # # from rest_framework.decorators import api_view
# # # from django.shortcuts import render
# # # import json 
# # # from upeoapp import models
# # # from django.http import JsonResponse
# # # from rest_framework.decorators import api_view
# # # from django.http import HttpResponse




# # # # @api_view(['POST'])

# # #     # body = request.POST
# # #     # print(body)
# # #     # data = {}
# # #     # try:
# # #     #     data = json.loads(body)
# # #     # except:
# # #     #     pass
# # #     # # print(data)
# # #     # data['headers'] = dict(request.headers)
# # #     # data['content_type'] = request.content_type
# # #     # return JsonResponse(data)
  
# # # def send_sms(request):
    
# # #     username = "sandbox"
# # #     api_key = "8249e0952263bd3663010ddb25d57840a65eefce53dc7c7499e4b50af2769a27"
# # #     # Initialize the SDK
# # #     africastalking.initialize(username, api_key)
# # #     # Get the SMS service
# # #     sms = africastalking.SMS
    
# # #     recipients = ["+254713520935"]
# # #     sender = "36291"

# # #     # Set your message
# # #     message = "Hello Learner,find the area of the triangle below.";
# # #     questions=models.Questions.objects.all()
    
        
# # #     for x in range(len(questions)):
# # #             print(questions[x])
# # #     quest=questions.question
    
# # #     message=f"Hello your question is {questions[x]}"

              
# # #     # Set your shortCode or senderId
# # #     # sender = "4632"
    
# # #     try:
# # #         body=request.get_json()['from']
# # #         print(body)
        
        

# # #         # response = sms.send(message, recipients)
        
# # #         return render(request,"test.html",{"response":response})
# # #     except Exception as e:
# #         # return render(request,"test.html",{"response":e})

# # import africastalking
# # from rest_framework.response import Response 
# # from rest_framework.decorators import api_view
# # from django.shortcuts import render
# # from upeoapp import models
  
# # def send(request):
# #     username = "Nakayiza"
# #     api_key = "ee4e8964e4c5b662483bf5a25b6af88a393a3ad5c1ead01ac7dcfbdd511e0dd0"

# #     # Initialize the SDK
# #     africastalking.initialize(username, api_key)
# #     # Get the SMS service
# #     sms = africastalking.SMS
    
# #     recipients = ["+254713520935","+254792903185"]
# #     sender = "shortCode or senderId"
# #     # +254 722 709900

# #     # Set your message
# #     # message = "Hello Learner,find the area of the triangle below.";
# #     questions=models.Questions.objects.all()
    
        
# #     for x in range(len(questions)):
# #             print(questions[x])
# #     # quest=questions.question
    
# #     message=f"{questions[x]}"

              
# #     # Set your shortCode or senderId
# #     # sender = "4632"
    
# #     try:
# #         response = sms.send(message, recipients)
        
# #         return render(request,"test.html",{"response":response})
# #     except Exception as e:
# #         return render(request,"test.html",{"response":e})

# import africastalking
# from rest_framework.response import Response 
# from rest_framework.decorators import api_view
# from django.shortcuts import render
# from upeoapp import models
# # I imported Rendom so as to use it to get x
# import random
  
# def send(request):
#     # return("sms is hit")
#     username = "Nakayiza"
#     api_key = "ee4e8964e4c5b662483bf5a25b6af88a393a3ad5c1ead01ac7dcfbdd511e0dd0"

#     # Initialize the SDK
#     africastalking.initialize(username, api_key)
#     # Get the SMS service
#     sms = africastalking.SMS
    
#     # Right aroung here youshould pass the recipients numbner, thats when u are in production
#     recipients = ["+254713520935"]
#     sender = "shortCode or senderId"

#     # Set your message
#     # message = "Hello Learner,find the area of the triangle below.";
#     questions=models.Questions.objects.all()
#     # return str(len(questions))
    
#     #this wil handle the question indexes
#     indexes = []    
#     #loop through the range of the questions' array and append them to the array
#     for x in range(len(questions)):
#             indexes.append(x)
#     question = questions[random.choice(indexes)] 
#     # quest=questions.question

    
#     message=f"Hello your question is {question}"
#     # return message

              
#     # Set your shortCode or senderId
#     # sender = "4632"
    
#     try:
#         response = sms.send(message, recipients)
        
#         return render(request,"test.html",{"response":response})
#     except Exception as e:
#         return render(request,"test.html",{"response":e})

import africastalking
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.shortcuts import render
from upeoapp import models
# I imported Rendom so as to use it to get x
import random
  
def send(request):
    # return("sms is hit")
    username = "Nakayiza"
    api_key = "ee4e8964e4c5b662483bf5a25b6af88a393a3ad5c1ead01ac7dcfbdd511e0dd0"

    # Initialize the SDK
    africastalking.initialize(username, api_key)
    # Get the SMS service
    sms = africastalking.SMS
    
    # Right aroung here youshould pass the recipients numbner, thats when u are in production
    recipients = ["+254111365595"]
    sender = "shortCode or senderId"

    # Set your message
    # message = "Hello Learner,find the area of the triangle below.";
    questions=models.Questions.objects.all()
    # return str(len(questions))
    
    #this wil handle the question indexes
    indexes = []    
    #loop through the range of the questions' array and append them to the array
    for x in range(len(questions)):
            indexes.append(x)
    question = questions[random.choice(indexes)] 
    # quest=questions.question

    
    message=f"{question}"
    # return message

              
    # Set your shortCode or senderId
    # sender = "4632"
    
    try:
        response = sms.send(message, recipients)
        
        return render(request,"test.html",{"response":response})
    except Exception as e:
        return render(request,"test.html",{"response":e})