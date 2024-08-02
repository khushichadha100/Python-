import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def preprocess_text(sentence):
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in sentence.split() if word.lower() not in stop_words]
    
    return dict([(word, True) for word in filtered_tokens])
# Training data - positive and negative sentences
positive_sentence = "This movie is great and awesome!"
negative_sentence = "The food was terrible and the service was bad."
positive_features = preprocess_text(positive_sentence)
negative_features = preprocess_text(negative_sentence)
# Combine features with labels
training_data = [
    (positive_features, 'Positive'),
    (negative_features, 'Negative')
]
# Train a Naive Bayes classifier
classifier = nltk.NaiveBayesClassifier.train(training_data)
# Test sentence to classify
test_sentence = "The movie was good but the food was awful."
# Preprocess test sentence
test_features = preprocess_text(test_sentence)
# Classify the test sentence
result = classifier.classify(test_features)
print("Test Sentence:", test_sentence)
print("Predicted Class:", result)
