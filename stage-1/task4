def hamming_distance(str1, str2):
    """
    Calculate the Hamming distance between two strings.
    
    Parameters:
    str1 (str): First string.
    str2 (str): Second string.
    
    Returns:
    int: Hamming distance between the two strings.
    """
    # Pad the shorter string with spaces to make lengths equal
    max_len = max(len(str1), len(str2))
    str1 = str1.ljust(max_len, ' ')
    str2 = str2.ljust(max_len, ' ')
    
    # Calculate Hamming distance
    distance = sum(c1 != c2 for c1, c2 in zip(str1, str2))
    return distance

# Example usage
slack_username = "Jose Valentim"
twitter_handle = "valentimfilho"

# Calculate Hamming distance
distance = hamming_distance(slack_username, twitter_handle)
print(f"Hamming distance between '{slack_username}' and '{twitter_handle}': {distance}")
