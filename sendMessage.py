# from heyoo import WhatsApp

# messenger = WhatsApp(token='EAAVxNUP2DEUBO5enEofqn8EaDZCHu19AKnRaMJ6rzA6PD7EFVNRxiEgSqIycONtwZCtifBC5IrfdjQGeQ6nko5SrkxGeOsxDGoIqZAPP8NDWw5mDreSUAEtcW5r3cs48FmOLvdy6yO5hKxLlZAqQDqo28GXCfcuMZAIIDi3eQObAlDZCUrxHZCXEogCu70Plwn5fef9ZBJDfyFoxJXwbhLAZD',phone_number_id='104751029397504')
# # For sending a Text messages
# response = messenger.send_message(message='Hello I am WhatsApp Cloud API', recipient_id='918588847669')

# print(response)


import requests

# Define the API endpoint URL
api_url = 'https://graph.facebook.com/v17.0/104751029397504/messages'

# Define the data you want to send in the POST request
data = {
   "messaging_product": "whatsapp", "to": "918588847669", "type": "template", "template": { "name": "watermarck", "language": { "code": "en_US" } } 
}

# Define custom headers
headers = {
    'Authorization': 'Bearer EAAVxNUP2DEUBO4hsKUWTqeTGaIBA7ZA0ZC5kgZCaZAYTd0TXA2zKsLD9h1VjMxJ0WfIuVUYc9n5487JJLusZAMdIuqaAmGBWRGZCYMVgs9BI5V2JTkZCZBuXfQajm2MZBELe65Jy6tPcg61pzcmRHXrxOOz6QZCqqM9GbLyNdpzBBFzqi1TCT13X1F1UpPSUsZB1ZAXHk6KZBFRI27E350g5QRDTE',
    'Content-Type': 'application/json',  # Specify the content type if needed
}

# Send a POST request to the API with custom headers
response = requests.post(api_url, json=data, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse and work with the API response data
    response_data = response.json()  # Assuming the response is in JSON format
    print(response_data)
else:
    # Handle the case where the API request was not successful
    print(f"API request failed with status code: {response.status_code}")
    print(response.text)  # Print the response content for debugging
