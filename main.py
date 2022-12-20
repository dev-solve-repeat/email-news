import requests

api_key = "3017c762b3f9426191584b31895aa972"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-11-20&sortBy=publishedAt&apiKey=" \
      "3017c762b3f9426191584b31895aa972"

# Get the request from the url
request = requests.get(url)

# Get the data in the form of dictionary
content = request.json()

# Access the article title and description
for article in content["articles"]:
    print("title:", article["title"])
    print("description:", article["description"])
