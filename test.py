from textblob import TextBlob
import os

def review_analyzer(reviewpath):
    positive_rev = []
    negative_rev = []
    neutral_rev = []
    processed_files = []

    for filename in os.listdir(reviewpath):
        if filename.endswith('.txt') and not filename.startswith('.'):
            file_path = os.path.join(reviewpath, filename)
            processed_files.append(file_path)
            with open(file_path, 'r', encoding='utf-8') as file:
                review_text = file.read()
                text = TextBlob(review_text)
                polarity = text.sentiment.polarity

                if polarity > 0:
                    positive_rev.append((file_path, review_text, polarity))
                elif polarity < 0:
                    negative_rev.append((file, review_text, polarity))
                elif polarity == 0:
                    neutral_rev.append((file, review_text, polarity))
            


    return positive_rev, negative_rev, neutral_rev, processed_files


pos_folder_path = 'D:/SFU WORK/Fall 2023/SDA 250/Assignment2/pos'
neg_folder_path = 'D:/SFU WORK/Fall 2023/SDA 250/Assignment2/neg'

result_pos = review_analyzer(pos_folder_path)
result_neg = review_analyzer(neg_folder_path)

positive_reviews = result_pos[0]
negative_reviews = result_neg[1]
neutral_reviews = result_neg[2]
processed_files = result_neg[3]

print(f"Number of positive reviews: {len(positive_reviews)}")
print(f"Number of negative reviews: {len(negative_reviews)}")
print(f"Number of neutral reviews: {len(neutral_reviews)}")
print(f"Total number of files processed: {len(result_pos[0]) + len(result_neg[1]) + len(result_neg[2])}")
print(f"Total number of files in the directory: {len(os.listdir(pos_folder_path)) + len(os.listdir(neg_folder_path))}")

for file_path in processed_files:
    print(f"Processed file: {file_path}")
