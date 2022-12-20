import requests
from send_email import send_emails

topic = "tesla"
# f should be added to the line where change needs to be made.
api_key = "3017c762b3f9426191584b31895aa972"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2022-11-20&" \
      "sortBy=publishedAt&" \
      "apiKey=3017c762b3f9426191584b31895aa972&" \
      "language=en" # for selecting the language

# Get the request from the url
request = requests.get(url)

# Get the data in the form of dictionary
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"][:20]: # for restricting to 20 news
    if article["title"] is not None:   # this is to remove the error is title value is None -
        # which is a None type in python
        # To add subject to the mail.
        body = "Subject: Todays News" + "\n" + \
               body + article["title"] + "\n"\
               + article["description"] + "\n"\
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_emails(message=body)




