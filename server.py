from flask import Flask, request

app = Flask(__name__)

@app.route('/send-discord-message', methods=['POST'])
def send_message():
  # Replace with your actual webhook URL and message content
  webhook_url = "https://discord.com/api/webhooks/1227323485001617508/2qwsvge6R-RXL1xxmjxNI65xPKPwMVcb0CuLBQQFVL1-uMJ0-37NLOydgqWsiHdn2ENa"
  message = "Hey! Someone just got rickrolled!"

  # Use a library like `requests` to send the POST request to Discord
  import requests
  payload = {
    "content": message
  }
  requests.post(webhook_url, json=payload)

  return "Message sent!"

if __name__ == '__main__':
  app.run()
