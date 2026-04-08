"""
02_02_self_attention.py
Project: Code a mini Transformer "Self-Attention" mechanism (Fuzzy Dictionary) from scratch.
"""
import math

def dot_product(vec1, vec2):
    """Calculates relationship mathematically between two arrays."""
    return sum(a * b for a, b in zip(vec1, vec2))

def softmax(scores):
    """Converts raw scores into percentages/probabilities that add up to 1.0 (100%)"""
    exp_scores = [math.exp(s) for s in scores]
    total = sum(exp_scores)
    return [s / total for s in exp_scores]

def create_mock_embeddings():
    """
    Imagine we embedded a sequence of three words into simple 3D arrays:
    Word 1: "Bank" (The ambiguous word)
    Word 2: "Money" (A financial clue)
    Word 3: "River" (A nature clue)
    """
    return {
        "Bank": [1.0, 0.0, 0.2],
        "Money": [0.9, 0.1, 0.0],
        "River": [0.0, 0.9, 0.8]
    }

def single_head_self_attention(query_word, sequence_embeddings):
    """
    A bare-bones Self-Attention mechanism.
    For simplicity, we assume Query=Key=Value=Embedding.
    """
    print(f"--- Self-Attention for '{query_word}' ---")
    
    query_vector = sequence_embeddings[query_word]
    
    # 1. Calculate Attention Scores (Dot Products between Query and all Keys)
    # This measures how "relevant" every other word is to our Query.
    raw_scores = []
    words_in_sequence = list(sequence_embeddings.keys())
    
    for word in words_in_sequence:
        key_vector = sequence_embeddings[word]
        score = dot_product(query_vector, key_vector)
        raw_scores.append(score)
        
    # Scale the scores (Standard transformer math usually divides by sqrt(dimensions))
    scaled_scores = [s / math.sqrt(len(query_vector)) for s in raw_scores]
    
    # 2. Turn scores into percentages using Softmax
    attention_weights = softmax(scaled_scores)
    
    print("Calculating context alignment (Attention Weights):")
    for word, weight in zip(words_in_sequence, attention_weights):
        print(f"  Focus placed on '{word}': {weight*100:.1f}%")
        
    # 3. Blend the Values together!
    # Multiply each word's embedding (Value) by how much attention we are paying to it.
    blended_vector = [0.0, 0.0, 0.0]
    for i in range(len(attention_weights)):
        target_value = sequence_embeddings[words_in_sequence[i]]
        weight = attention_weights[i]
        
        blended_vector[0] += target_value[0] * weight
        blended_vector[1] += target_value[1] * weight
        blended_vector[2] += target_value[2] * weight
        
    print(f"\nFinal Blended Context Vector for '{query_word}':")
    print([round(val, 3) for val in blended_vector])
    print()
    print("Notice how 'Bank' blended heavily with 'Money' due to their vector similarity, altering its final mathematical meaning to represent a financial institution rather than a river bank!")

if __name__ == "__main__":
    embeddings = create_mock_embeddings()
    single_head_self_attention("Bank", embeddings)
