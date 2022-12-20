import requests
from send_email import send_emails

api_key = "3017c762b3f9426191584b31895aa972"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-11-20&sortBy=publishedAt&apiKey=" \
      "3017c762b3f9426191584b31895aa972"

# Get the request from the url
request = requests.get(url)

# Get the data in the form of dictionary
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:   # this is to remove the error is title value is None -
        # which is a None type in python
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_emails(message=body)




