# Naive Bayes Classifier
Naive Bayes Classifier for a corpus of tweets (Railway Budget) into 3 sentiment classes :
  - Positive
  - Negative
  - Neutral

##### Notes:
1. The training and test data was manually labelled into three sentiment classes.
2. The prior probablity was calculated for both the data sets.

##### Steps:
###### Part A: Cleaning

1. The data set was cleaned for Hashtags, URLs, RT, Usernames with the help of PLY module
2. The emoticons were categorized into 3 classes: happy, sad and neutral (PLY)
3. The slang was removed. (one cause for lower accuracy)

###### Part B: Using nltk

1. Changing the case of the text to lowercase
2. Removing stop words by using the nltk.corpus.stopwords.words() module
3. Stemming the wordlist using Porter Stemmer
4. Lemmatizing the wordlist using WordNetLemmatizer() function

###### Part C: Calculating probabilities

1. Each word in a particular tweet will be associated with a probabilty of being in a sentiment class. This is done by using the formula
                `P(word[i]|Class) = (count(word[i],Class)+1)/(Summation(count (word[i],all))+mod(Vocab))`
2. Each word's sentiment probabilty is calculated
3. argmax is then calculated
4. The probability is converted to log due to the fact that the probabilities gets very small on multiplying.
                `(log(x*y) = log(x)+log(y))`

###### Part D: Comparing with manual

1. The new tweet is cleaned and preprocessed
2. The trained values are compared and the argmax is calculated and the sentiment of a tweet can thus be arrived

##### Performance:
* Program gives an accuracy of 65%.
* For tweets which contains too much of nouns, hindi-english words, numbers this code won't produce good results
* Since training dataset contained lots of nouns like name, place, etc, hence this inaccuracy
