import requests

webhookurl= "paste"
# paste your webhook Url here

def send(message):
    msg = {
        "content": message,
        "username": "Python Bot"
    }

    response = requests.post(
        webhookurl,
        json=msg,
        timeout=15
    )

    if response.status_code == 204:
       print("sent")
    else:
        print("didnt send, send again", response.status_code)
        print(response.text)


send("hi")
