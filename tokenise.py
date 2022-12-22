import nltk
import collections
import re
import string
import pandas as pd
import csv

from collections import Counter
from nltk import FreqDist

nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open("D:/VSC/morrieCh1_TheCurriculum.txt", encoding = "utf8") as f:
    text = f.read()
    print(text)

def clean_text(text):
    #convert to lower case
    cleaned_text = text.lower()
    #remove HTML tags
    html_pattern = re.compile("<.*?>")
    cleaned_text = re.sub(html_pattern, "", cleaned_text)
    #remove punctuations
    cleaned_text = cleaned_text.translate(str.maketrans("","", string.punctuation))
    return cleaned_text.strip()

def no_number_preprocessor(tokens):
    r = re.sub("(\d)+", "", tokens)
    return r

no_num_text = no_number_preprocessor(text)
print(no_num_text)

#list of stopwords
stopwords_ls = list(set(stopwords.words("english")))
print("Total English stopwords: ", len(stopwords_ls))
print(stopwords_ls)

#add my own stopwords
my_extra = ["a", "an", "the", "this", "that", "is", "it", "to", "and", "in", "for", "on", "of", "be", "as", "by", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
stopwords_ls.extend(my_extra)

cleaned_text = clean_text(no_num_text)
print(cleaned_text)

filtered_list = []

wordtokens = word_tokenize(cleaned_text)
print(wordtokens)

for w in wordtokens:
    if w not in stopwords_ls:
        filtered_list.append(w)

filtered_list

#for counting tokenized words
collections.Counter(filtered_list)

#converting into a list of words and their frequencies
cnt = Counter(filtered_list)
wordlist = [list(i) for i in cnt.items()]
print(wordlist)

#converting list into a dataframe
df = pd.DataFrame(data = wordlist, columns = ["word", "count"])
print(df)

#exporting wordlist
df.to_csv("D:/VSC/morrieCh1_TheCurriculum.csv", index = False, encoding = "utf-8")