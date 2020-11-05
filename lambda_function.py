import json

def lambda_handler(events, context):

# events: It is a object which invoked lambda functio to trigger either manually or by other aws function
# context: contain meta-data of lamda function
   return {
       "context function name":json.dumps(context.function_name)
   }

