import re

def clean_word(word):
    """Remove references (comma followed by a number or letter at the end of a word)."""
    return re.sub(r",[a-zA-Z0-9]+$", "", word)

def has_five_unique_letters(word):
    """Check if a word contains at least five different letters (excluding special characters except space, hyphen, apostrophe, and extended Latin letters)."""
    # allowed_chars = "a-zA-ZæøåéüàöíêèóâôïñçûùáìîäëÿžščßœłđðŋŧÆØÅÉÜÀÖÍÊÈÓÂÔÏÑÇÛÙÁÌÎÄËŸŽŠČŁĐÐŊŦ"
    allowed_chars = "a-zA-ZæøåÆØÅ"
    cleaned_word = re.sub(fr"[^{allowed_chars}]", "", word)  # Remove unwanted special characters
    return len(set(cleaned_word)) >= 5

def filter_words(input_file, output_file, removed_file):
    """Filter words that contain at least five different letters, removing words with numbers and special characters (except allowed ones)."""
    # allowed_chars = "a-zA-ZæøåéüàöíêèóâôïñçûùáìîäëÿžščßœłđðŋŧÆØÅÉÜÀÖÍÊÈÓÂÔÏÑÇÛÙÁÌÎÄËŸŽŠČŁĐÐŊŦ' -"
    allowed_chars = "a-zA-ZæøåÆØÅ' -"
    
    with open(input_file, "r", encoding="ISO-8859-1") as file:
        words = file.read().splitlines()
    
    filtered_words = []
    removed_words = []
    
    for word in words:
        cleaned_word = clean_word(word)  # Remove references
        if re.search(r"[0-9]", cleaned_word) or re.search(fr"[^{allowed_chars}]", cleaned_word):
            removed_words.append(word)
        elif has_five_unique_letters(cleaned_word):
            filtered_words.append(cleaned_word)
    
    # Save filtered words
    with open(output_file, "w", encoding="ISO-8859-1") as file:
        file.write("\n".join(filtered_words))
    
    # Save removed words
    with open(removed_file, "w", encoding="ISO-8859-1") as file:
        file.write("\n".join(removed_words))
    
    print(f"Filtered words saved to {output_file}")
    print(f"Removed words saved to {removed_file}")

# Example usage
if __name__ == "__main__":
    input_file = "ordnet.txt"  # Change this to your actual file name
    output_file = "filtered_words.txt"
    removed_file = "removed_words.txt"
    filter_words(input_file, output_file, removed_file)