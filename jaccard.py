from parser import get_all_texts
def jaccard_similarity(text1, text2):
    set1, set2 = set(text1.split()), set(text2.split())
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0

def find_top_similar_texts(text_list, target_text, top_n=3):
    """Find the top N most similar texts from text_list using Jaccard similarity."""
    # Calculate Jaccard similarity for each text in the list
    similarities = [(text, jaccard_similarity(text, target_text)) for text in text_list]
    
    # Sort texts by similarity score in descending order
    sorted_texts = sorted(similarities, key=lambda x: x[1], reverse=True)
    
    # Select the top N texts based on the similarity score
    top_texts = sorted_texts[:min(top_n, len(text_list))]

    # Return only the texts from the tuples
    return [text for text, score in top_texts]

def optimal_text(base_url, target):
    # Assume get_all_texts(base_url) retrieves all texts from the given base URL
    texts = get_all_texts(base_url)
    
    # Find the top 5 most similar texts
    top_texts = find_top_similar_texts(texts, target)
    
    # Combine the top similar texts into a single unique text
    combined_text = " ".join(top_texts)
    
    return combined_text
# Example usage
if __name__ == "__main__":
    base_url  = "https://asvas-organization.gitbook.io/koboto-network-interface"
    target = '''
    The Application Contract receives the consumer’s request and then relays it to the Domain Coordinator contract on koboto . The Domain Coordinator is responsible for managing the overall workflow and coordinating the interactions between the on-chain and off-chain components.

    '''
    print ("most similar:")
    print (optimal_text (base_url, target))
