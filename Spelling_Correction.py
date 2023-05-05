# Install textblob module if it is not install in your system already 
# pip install -U textblob

#Import the required module
import textblob 
from textblob import TextBlob
def Convert (string):
    li=list(string.split())
    return li
str1=input("Enter the word:  ")
words=Convert(str1)
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")