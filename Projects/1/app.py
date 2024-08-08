import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import re
import string
import os

# Load models
PATH = os.path.join("constants", "interview_qna_scoring_model")
loaded_model = tf.saved_model.load(PATH)
use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Preprocessing functions
def split_words(text):
    """
    Splits the input text into individual words and punctuation marks.
    """
    words = re.findall(r'\w+|[^\w\s]', text)
    return words

def merge(l1, l2):
    """
    Merges two sorted lists into a single sorted list, removing duplicate words.
    """
    merged = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        word1, word2 = l1[i], l2[j]
        if word1 in string.punctuation:
            i += 1
        elif word2 in string.punctuation:
            j += 1
        elif word1 == word2:
            merged.append(word1)
            i += 1
            j += 1
        else:
            merged.append(word1)
            i += 1
    while i < len(l1):
        if l1[i] not in string.punctuation:
            merged.append(l1[i])
        i += 1
    while j < len(l2):
        if l2[j] not in string.punctuation:
            merged.append(l2[j])
        j += 1
    return merged

def preprocess(text):
    """
    Preprocesses the input text by splitting it into individual words and merging them into sentences.
    """
    text = text.lower()
    sentences = []
    lines = text.split('\n')
    for line in lines:
        words = split_words(line)
        sentences = merge(sentences, words)
    return ' '.join(sentences)

def refine(text):
    """
    Refines the input text by concatenating incomplete words.
    """
    refined_text = ""
    words = text.split()
    i, n = 0, len(words)
    while i < n:
        w1 = words[i]
        if i < n - 1:
            w2 = words[i + 1]
            if w1.startswith(w2):
                refined_text += w1 + " "
                i += 2
            elif w2.startswith(w1):
                refined_text += w2 + " "
                i += 2
            else:
                refined_text += w1 + " "
                i += 1
        else:
            refined_text += w1
            i += 1
    return refined_text.strip()

def sentences_encoder(sentences):
    """
    Encodes sentences using the Universal Sentence Encoder.
    """
    sentence_vectors = use_model(sentences)
    return sentence_vectors

def predict(question, answer):
    """
    Predicts the score for a given question and answer pair.
    """
    answer = preprocess(answer)
    answer = refine(answer)
    input_text = f"Question: {question} \n Answer: {answer}"
    embeddings = sentences_encoder([input_text, ""])
    predictions = loaded_model(embeddings)
    score = predictions[0].numpy()[0]
    return max(0, min(100, score))

# Example usage
# question = "Describe who you are?"
# answer = "I am a dedicated professional with five years of experience in marketing and a passion for creativity."
# print("Predicted Score:", predict(question, answer))
