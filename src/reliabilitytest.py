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
# print(json.dumps(data, indent=4))
print("\n!!! Each article begins with a 50 percent reliability score, as we view the source from an unbiased standpoint. !!!")
score = 50
print(f'\nThe article in question is titled "{soup.title.text}", written by {data["author"]["name"]}.')
print(f'Read more about {data["author"]["name"]} and their other work to determine their reliability: {data["author"]["url"]}\n')

print(f'This website is a(n) {data["publisher"]["@type"]}!')
if ".com" in url:
    score -= 15
    print(f"Since this article is derived from a website with a commercial aspect, its score is now a {score}.\n")
elif ".org" in url:
    score += 15
    print(f"Since your article is derived from a website associated with an organization, its score is now a {score}.\n")
elif ".gov" in url:
    score += 25
    print(f"Since your article is derived from a government-affiliated website, its score is now a {score}.\n")
elif ".edu" in url:
    score += 35
    print(f"Since your article is dervied from an educational website, perfect for academic work, its score is now a {score}.\n")

datePublished = data["datePublished"]
dateModified = data["dateModified"]
print(f"Date of publication: {datePublished}")
print(f"Date of modification: {dateModified}")
if datePublished != dateModified:
    score += 20
    print(f"Because your article has been updated since its publication, your reliability score is now a {score}.\n")
else:
    score -= 20
    print(f"Because your article has not been updated since its publication, your score is now a {score}.\n")

publisher = data["publisher"]["name"]
pub_url = data["publisher"]["url"]
print(f"The publisher of your article is {publisher}. Read more about this publisher here to determine their reliability: {pub_url}.\n")

print(f"Through a quick analysis of your article in question, the reliability score is determined to be a {score}. However, it's important to follow through with research of your own, both on the author(s) and the publisher, to fully determine whether or not the information presented is trustworthy to use in further research.")

