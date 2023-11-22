from textblob import TextBlob
import os
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics

def review_analyzer_only_positive(reviewpath):
    positive_rev = []
    for filename in os.listdir(reviewpath):
        if filename.endswith('.txt') and not filename.startswith('.'):
            file_path = os.path.join(reviewpath, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                review_text = file.read()

                # all documents are labeled as positive
                positive_rev.append(('positive', filename))

    return positive_rev
folder_path_positive = 'pos'
positive_reviews_only = review_analyzer_only_positive(folder_path_positive)



def review_analyzer_only_negative(reviewpath):
    negative_rev = []
    for filename in os.listdir(reviewpath):
        if filename.endswith('.txt') and not filename.startswith('.'):
            file_path = os.path.join(reviewpath, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                review_text = file.read()

                # all documents are labeled as positive
                negative_rev.append(('negative', filename))

    return negative_rev
folder_path_negative = 'neg'
negative_reviews_only = review_analyzer_only_negative(folder_path_negative)


labeled_reviews = positive_reviews_only + negative_reviews_only
random.shuffle(labeled_reviews)

len_all_files = len(labeled_reviews)
len_training = int(len_all_files * 0.8)
len_test = int(len_all_files * 0.2)

# breaks the labeled reviews into training and test sets
trainingrevs = labeled_reviews[:len_training]
testrevs = labeled_reviews[len_training:]

# extracts review text from each tuple in trainingrevs and testrevs
train_text = [review_text for _, review_text in trainingrevs]
test_text = [review_text for _, review_text in testrevs]

# extracts labels from each tuple in trainingrevs and testrevs
train_labels = [sentiment for sentiment, _ in trainingrevs]
test_labels = [sentiment for sentiment, _ in testrevs]

def review_analyzer(review_data):
    positive_rev = []
    negative_rev = []
    neutral_rev = []

    for sentiment, review_text in review_data:
        text = TextBlob(review_text)
        polarity = text.sentiment.polarity

        if polarity > 0:
            positive_rev.append(('positive', review_text, polarity))
        elif polarity < 0:
            negative_rev.append(('negative', review_text, polarity))
        else:
            neutral_rev.append(('neutral', review_text, polarity))

    return positive_rev, negative_rev, neutral_rev

# this will analyze the sentiment of the training set
positive_reviews_train, negative_reviews_train, neutral_reviews_train = review_analyzer(trainingrevs)

# this will analyze the sentiment of the test set
positive_reviews_test, negative_reviews_test, neutral_reviews_test = review_analyzer(testrevs)

# creates a vector and uses naive bayes classifier method for training
model = make_pipeline(CountVectorizer(), MultinomialNB())

# this should train the model
model.fit(train_text, train_labels)

# makes a prediction for the model and helps with the accuracy calculation
predictions = model.predict(test_text)

# prints the accuracy of the model
accuracy = metrics.accuracy_score(test_labels, predictions)
print(f"Accuracy on the test set: {accuracy}")