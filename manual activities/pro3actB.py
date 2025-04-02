def merge_dictionaries(dict1, dict2):
    """Merges two dictionaries, adding values for overlapping keys."""
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Add values if key exists in both dictionaries
        else:
            merged_dict[key] = value  # Otherwise, just add the new key-value pair
    
    return merged_dict

# Test the function
dict1 = {"apple": 5, "banana": 3, "orange": 2}
dict2 = {"banana": 4, "orange": 1, "grape": 7}

merged_dict = merge_dictionaries(dict1, dict2)

# Display results
print("Merged Dictionary:", merged_dict)
