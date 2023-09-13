import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
# print(lower_case)
# print(string.punctuation)
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
# print(cleaned_text)
# tokenised_words= cleaned_text.split()
tokenised_words = word_tokenize(cleaned_text, "english")
# print(tokenised_words)
'''stop_words =  ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]'''
final_words = []
for word in tokenised_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# print(final_words)
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)
        # print("Word:"+word+"  "+"Emotion:"+emotion)
        # print(clear_line)
        # print(line)

print(emotion_list)
w = Counter(emotion_list)
print(w)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    if neg > pos: 
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Vibe")


sentiment_analyse(cleaned_text)
fig, axl = plt.subplots()
# plt.bar(w.keys(),w.values())
axl.bar(w.keys(), w.values())
fig.autofmt_xdate()

plt.savefig('graph.png')
plt.show()
