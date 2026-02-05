import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample training data
texts = [
    "I love this product",
    "This is amazing",
    "Very happy with the service",
    "I hate this",
    "This is terrible",
    "Very bad experience"
]

labels = [1, 1, 1, 0, 0, 0]  # 1 = Positive, 0 = Negative

# Tokenization
tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Padding
X = pad_sequences(sequences, maxlen=10)
y = tf.convert_to_tensor(labels)

# LSTM Model
model = Sequential([
    Embedding(input_dim=1000, output_dim=16, input_length=10),
    LSTM(32),
    Dense(1, activation="sigmoid")
])

# Compile
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train
model.fit(X, y, epochs=30, verbose=1)

# -------- USER INPUT --------
print("\n--- Sentiment Prediction ---")
user_text = input("Enter a sentence: ")

user_seq = tokenizer.texts_to_sequences([user_text])
user_pad = pad_sequences(user_seq, maxlen=10)

prediction = model.predict(user_pad)

if prediction[0][0] >= 0.5:
    print("Sentiment: POSITIVE 😊")
else:
    print("Sentiment: NEGATIVE 😠")
