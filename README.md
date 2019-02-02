# Restfulapi
RESTful web service that schedules messages to be printed. The web service should accept a message content and delivery time. The web service should return 202 status code (accepted) if the message was successfully scheduled. The web service should print the message content on the console at the delivery time specified.
Framework used->Flask
Module used->Flask , request, jsonify,flask_api
IDE->Pycharm(coding)
Tool->Postman(testing)
How it works:--
             We have creted two resources one for getting message and time as input from user and other one is to put status code.
How to Test:--
             How to schedule time/message:-
             ->select POST Method
                -->Hit the URL->http://127.0.0.1:5000/setmessage/
                  -->select Header and put content type as application/json
                                
                   -->Select Body-> Give request parameter as below example:
                                    {
	                                      "time" : "56",
	                                      "message" : "Gud Morning"
                                      }
                      if other message is already scheduled at given time it will return status code 400 with message : 
                          {'already scedule': 'this time is already schedule for other message'}
                      if no message schedule at the given time it will scedule the message and return status code 202 with message : 
                          {202: 'the requested message scedule for give time'}
                
                                      
             How to get schedule message and message is scheduled or not:-
             ->select GET Methos
               -->Hit the URL->http://127.0.0.1:5000/getmessage/{time_value}
                   if any message schedule for the given time it will return the message with status code 200 and print the message.
                   else it will return status code 404 and print below message:
                       {"message not present": "Message not present for the requested time"}

             
  Code to run-->rest.py
             
             
