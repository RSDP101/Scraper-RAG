from parser import get_all_texts
def jaccard_similarity(text1, text2):
    """Compute Jaccard similarity between two texts."""
    # Convert the texts to sets of words (removing duplicates)
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())

    # Compute the intersection and union of the two sets
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    # Return the Jaccard similarity metric
    return len(intersection) / len(union)


def find_most_similar_text(text_list, target_text):
    """Find the text from text_list most similar to target_text using Jaccard similarity."""
    # Calculate Jaccard similarity for each text in the list
    similarities = [(text, jaccard_similarity(text, target_text)) for text in text_list]
    
    # Find the text with the highest similarity score
    most_similar_text = max(similarities, key=lambda x: x[1])

    # Return the most similar text
    return most_similar_text[0], most_similar_text[1]

def optimal_text ( base_url, target):
    texts =get_all_texts(base_url)
    most_similar, similarity_score = find_most_similar_text(texts, target)
    return most_similar


# Example usage
if __name__ == "__main__":
    base_url  = "https://asvas-organization.gitbook.io/koboto-network-interface"
    target = '''
    The Application Contract receives the consumer’s request and then relays it to the Domain Coordinator contract on koboto . The Domain Coordinator is responsible for managing the overall workflow and coordinating the interactions between the on-chain and off-chain components.

    '''
    print ("most similar:")
    print (optimal_text (base_url, target))
