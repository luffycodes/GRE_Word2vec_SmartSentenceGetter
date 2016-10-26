# GRE_Word2vec_SmartSentenceGetter
Get sentences for words based on their broad categories. Automatically categorizes the words in following categories - art, culture, fiction, news, business, sports, medicine, science, technology. Hits vocabulary.com (https://www.vocabulary.com/) API to get them using a GET call.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 2.7.0
- Gensim (https://radimrehurek.com/gensim/install.html)

### Installing
#### Setup 
##### Downloads a text file to train initial word2vec model. Use more data to increase accuracy.
```
wget http://mattmahoney.net/dc/text8.zip -P /tmp
unzip /tmp/text8.zip
py word2vecModelGenerator.py
```
#### Runs trained word2vec model & hits server to fetch sentences
```
py getSmartSentencesForWords.py
```
