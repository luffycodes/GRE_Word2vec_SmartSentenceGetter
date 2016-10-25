import json
import requests
import gensim.models

model = gensim.models.Word2Vec.load('/home/shashank/Downloads/model')
categories = ['art', 'culture', 'fiction', 'news', 'business', 'sports', 'medicine', 'science', 'technology']

def find_word_category(candidate):
    matching_category = None
    cosine = 0
    for category in categories:
        category_similarity = model.n_similarity(category, candidate)
        if category_similarity > cosine:
            matching_category = category
            cosine = category_similarity
    return matching_category

def category_enum(category):
    if category == 'science':
        tag = 'M'
    elif category == 'culture':
        tag = 'A'
    else:
        tag = category[0].upper()
    return tag


words = ['football']

for word in words:
    closest_category = find_word_category([word])
    print(closest_category)
    if closest_category is None:
        url = "https://corpus.vocabulary.com/api/1.0/examples.json?maxResults=1&startOffset=0&query=%s" % (word)
    else:
        url = "https://corpus.vocabulary.com/api/1.0/examples.json?maxResults=1&startOffset=0&domain=%s&query=%s" % (category_enum(closest_category), word)
    print(url)
    data = requests.get(url).content
    jsonResponse = json.loads(data)
    try:
        jsonData = jsonResponse["result"].get("sentences")
        if len(jsonData) == 0:
            print(word + "::EMPTY")
        for item in jsonData:
            print(word + "::" + item.get("sentence"))
    except:
        print(word + "::NULL")
