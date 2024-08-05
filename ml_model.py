from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from load_data import preprocess_data, dialogue_pairs

# Extract inputs and outputs
inputs, outputs = zip(*dialogue_pairs)

# Vectorize text data
vectorizer = CountVectorizer().fit(inputs + outputs)
input_vectors = vectorizer.transform(inputs)
output_vectors = vectorizer.transform(outputs)

# Define a response function
def get_response(user_input):
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, input_vectors)
    closest = np.argmax(similarities, axis=1)
    return outputs[closest[0]]

# Test the response function
print(get_response("Could you BE any more excited?"))
