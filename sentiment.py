from textblob import TextBlob
import os

def review_analyzer(reviewpath):
    positive_rev = []
    negative_rev = []
    neutral_rev = []

    for filename in os.listdir(reviewpath):
        if filename.endswith('.txt') and not filename.startswith('.'):
            file_path = os.path.join(reviewpath, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                review_text = file.read()
                text = TextBlob(review_text)
                polarity = text.sentiment.polarity

                if polarity > 0:
                    positive_rev.append((file_path, review_text, polarity))
                elif polarity < 0:
                    negative_rev.append((file, review_text, polarity))
                else:
                    neutral_rev.append((file, review_text, polarity))

    return positive_rev, negative_rev, neutral_rev


folder_path = 'D:/SFU WORK/Fall 2023/SDA 250/Assignment_2/combined'


positive_reviews, negative_reviews, neutral_reviews = review_analyzer(folder_path)


print(f"Number of positive reviews: {len(positive_reviews)}")
print(f"Number of negative reviews: {len(negative_reviews)}")
print(f"Number of neutral reviews: {len(neutral_reviews)}")

