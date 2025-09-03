def generate_permutations(string):
    """
    Generate all permutations of a given string without using any libraries.
    
    Args:
        string (str): The input string.

    Returns:
        list: A list containing all permutations of the string.
    """
    # Base case: if the string has 0 or 1 character, return it as the only permutation
    if len(string) <= 1:
        return [string]

    permutations = []
    for i in range(len(string)):
        char = string[i]  # Current character
        remaining_string = string[:i] + string[i+1:]  # Remaining string without current character
        # Recursively generate all permutations of the remaining string
        for perm in generate_permutations(remaining_string):
            permutations.append(char + perm)  # Prepend current character

    return permutations


def main():
    string = input("Enter a string: ")
    permutations = generate_permutations(string)
    
    print(f"\nAll permutations of '{string}':")
    for perm in permutations:
        print(perm)
    
    print(f"\nTotal permutations: {len(permutations)}")


if __name__ == "__main__":
    main()
