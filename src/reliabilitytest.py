import json
import requests
from bs4 import BeautifulSoup

# print(json.dumps(data, indent=4))
#print("Title:", soup.title.text)
#print("Publisher:", data["publisher"]["name"])
#print("Date published:", data["datePublished"])
#print("Data modified:", data["dateModified"])
#print("Author:", data["author"]["name"])
#print("URL:", data["author"]["url"])

url = input("Enter a URL, and I will evaluate the source for its reliability!\nURL: ")
soup = BeautifulSoup(requests.get(url).content, "html.parser")
data = json.loads(soup.select_one('[type="application/ld+json"]').contents[0])
print(json.dumps(data, indent=4))
print("\n!!! Each article begins with a 50 percent reliability score, as we view the source from an unbiased standpoint. !!!")
print(f'\nThe article in question is titled "{soup.title.text}", written by {data["author"]["name"]}.')
print(f'Read more about {data["author"]["name"]}, as well as their other work, to determine their reliability: {data["author"]["url"]}')


print(f'\nThis website is a(n) {data["publisher"]["@type"]}')

