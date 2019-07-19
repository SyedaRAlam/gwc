'''
In this program, we print out all the text data from our twitter JSON file.

Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt
# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)
# # We can close the file now that we have locally stored the data.
tweetFile.close()


# tb = TextBlob("You are a brilliant computor Scientist")
# print(tb.polairty)

# print(type(tweetData))
# print(tweetData['favorite_count'])
#list(newdic.keys())

#favorite_count average
# fave = 0
# num = 0
# for item in tweetData:
# 	if "favorite_count" in item:
# 		fave += item["favorite_count"]
# 		num += 1
# avg = fave/num
# print("the avg is:")
# print(avg)

texts = []
for item in range(0,len(tweetData)):
	texts.append(tweetData[item]["text"])
# print(texts)
# print(len(texts))
# for t in range(0,len(texts)):
	# print(texts[t])
# print(texts[0])
# polarity_list = []
# for i in texts:
# 	blob1 = TextBlob(i)
# 	polar1 = blob1.polarity
# 	polarity_list.append(polar1)
# print(polarity_list)
def countLetter(string, letter):
	counter = 0
	for let in string:
		if let.lower() == letter:
			counter += 1
		else:
			counter += 0
	return counter


for i in range(0, len(tweetData)):
	texts.append(tweetData[i]["text"])

def wordCount(StringOfTweet, string1):
	counter = 0
	string1 = string1.lower()
	wordList = StringOfTweet.split(" ")
	for item in wordList:
		if item == string1:
			counter += 1
	return counter

wordCountList = []
for item in texts:
	wordoccurence = wordCount(item, "the")
	wordCountList.append(wordoccurence)


# print(countLetter("A") * 8, a)
tweetstring = " "
for tweet in texts:
	tweet = tweet + " "
	tweetstring += tweet

print(countLetter(tweetstring, "a"))
alpha = "qwertyuiopasdfghjklzxcvbnm"
letters = sorted(alpha)
print(len(set(sorted(alpha))))

for letter in letters:
	print(f"letter: {letter} occurences:{countLetter(tweetstring, letter)}")



occurences = []
for letter in letters:
	occurences.append(countLetter(tweetstring, letter))
print(occurences)
print(min(occurences), max(occurences))
plt.hist(occurences)
plt.axis([min(occurences), max(occurences),0, 10])
plt.show()


wordcloud = wordCloud(height = 1000, width = 1000).generate(tweetstring)
plt. figure(figsize = (10 , 10), facecolor = None)
plt.imshow(wordcloud, interpolation = "bilinear")
plt.show()
plt.savefig("alischart.png")















# print(list(tweetData[2].keys()))
# #['created_at', 'favorite_count', 'hashtags', 'id', 'id_str', 'lang', 'retweet_count', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions']
#
# print(tweetData[0]["favorite_count"])
#
#
#
#

#
# # We then print the data of ONE tweet:
# # the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.
