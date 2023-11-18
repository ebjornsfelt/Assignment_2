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


pos_folder_path = 'D:/SFU WORK/Fall 2023/SDA 250/Assignment2/pos'
neg_folder_path = 'D:/SFU WORK/Fall 2023/SDA 250/Assignment2/neg'

positive_reviews, negative_reviews, neutral_reviews = review_analyzer(pos_folder_path)

# Print the results
print(f"Number of positive reviews: {len(positive_reviews)}")
print(f"Number of negative reviews: {len(negative_reviews)}")
print(f"Number of neutral reviews: {len(neutral_reviews)}")

# print("Negative folder analysis:")
# for filename in os.listdir(neg_folder_path):
#     print(filename)
                
                
#                 if blob.sentiment.polarity > 0:
#                     positive_rev.append(review_text)
#                 elif blob.sentiment.polarity < 0:
#                     negative_rev.append(review_text)

#     return positive_rev, negative_rev

# # Specify the paths to the positive and negative review folders
# pos_folder_path = r'D:\SFU WORK\Fall 2023\SDA 250\Assignment2\pos'
# neg_folder_path = r'D:\SFU WORK\Fall 2023\SDA 250\Assignment2\neg'

# # Analyze positive reviews
# positive_reviews, negative_reviews = review_analyzer(pos_folder_path)

# # Analyze negative reviews
# positive_reviews, negative_reviews = review_analyzer(neg_folder_path)

# # Print the results
# print(f"Number of positive reviews: {len(positive_reviews)}")
# print(f"Number of negative reviews: {len(negative_reviews)}")