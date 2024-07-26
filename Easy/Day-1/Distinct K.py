def kth_unique_string(strings, k):
    """
    Function to find the kth unique string from a list of strings.
    
    :param strings: List of strings
    :param k: The kth position to find the unique string
    :return: The kth unique string or an empty string if there are less than k unique strings
    """
    # Dictionary to store the frequency of each string
    frequency = {}
    
    # List to store the order of unique strings
    unique_strings = []
    
    # Count the frequency of each string
    for string in strings:
        if string in frequency:
            frequency[string] += 1
        else:
            frequency[string] = 1
    
    # Collect the unique strings in the order they appear
    for string in strings:
        if frequency[string] == 1:
            unique_strings.append(string)
    
    # Check if there are at least k unique strings
    if len(unique_strings) >= k:
        return unique_strings[k-1]
    else:
        return ""

# Input reading
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    strings = data[1:N+1]
    k = int(data[N+1])
    
    # Find the kth unique string
    result = kth_unique_string(strings, k)
    
    # Print the result
    print(result)
