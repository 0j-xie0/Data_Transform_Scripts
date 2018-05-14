import read
import collections
df = read.load_data()
long_string = ""
for index, row in df.iterrows():
    long_string += str(row["headline"])
    
#convert to lowercase to make word count unique
long_string = long_string.lower()   
words_all = long_string.split(" ")
hundred_words = collections.Counter(words_all).most_common(100)
print(hundred_words)