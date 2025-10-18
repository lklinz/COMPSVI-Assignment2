import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    
    This is your first recursion problem. Think about:
    - Base case: What's the sum of an empty list?
    - Recursive case: If you know the sum of the rest of the list,
      how do you include the first number?
    
    Args:
        numbers (list): List of numbers to sum
    
    Returns:
        int: Sum of all numbers in the list
    
    Example:
        sum_list([1, 2, 3, 4]) should return 10
        sum_list([]) should return 0
    """
    # TODO: Implement this function
    # Hint: if len(numbers) == 0, return 0
    # Otherwise, return numbers[0] + sum_list(numbers[1:])

    # base case
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

# Test sum_list
print("\nTest sum_list:")
print(f"  sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])} (expected: 10)")
print(f"  sum_list([]) = {sum_list([])} (expected: 0)")
print(f"  sum_list([5, 5, 5]) = {sum_list([5, 5, 5])} (expected: 15)")

def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    
    This teaches you how to count items that match a condition.
    You'll use this same pattern for counting files!
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int: Count of even numbers in the list
    
    Example:
        count_even([1, 2, 3, 4, 5, 6]) should return 3
        count_even([1, 3, 5]) should return 0
    """
    # TODO: Implement this function
    # Hint: Base case is empty list (return 0)
    # If first number is even, add 1 to count from rest of list
    # If first number is odd, just return count from rest of list

    # Base Case
    if len(numbers) == 0:
        return 0
    else:
        if numbers[0] % 2 == 0:
            return 1 + count_even(numbers[1:])
        else:
            return count_even(numbers[1:])

# Test count_even
print("\nTest count_even:")
print(f"  count_even([1, 2, 3, 4, 5, 6]) = {count_even([1, 2, 3, 4, 5, 6])} (expected: 3)")
print(f"  count_even([1, 3, 5]) = {count_even([1, 3, 5])} (expected: 0)")
print(f"  count_even([2, 4, 6]) = {count_even([2, 4, 6])} (expected: 3)")

def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    
    This teaches you how to build a list of items that match a condition.
    You'll use this same pattern for finding infected files!
    
    Args:
        strings (list): List of strings to search
        target (str): Substring to search for
    
    Returns:
        list: All strings that contain the target substring
    
    Example:
        find_strings_with(["hello", "world", "help"], "hel") 
        should return ["hello", "help"]
    """
    # TODO: Implement this function
    # Hint: Base case is empty list (return [])
    # If first string contains target, add it to results from rest of list
    # Otherwise, just return results from rest of list
    # Use: if target in strings[0]

    # Base Case
    if len(strings) == 0:
        return []
    else:
        if target in strings[0]:
            return [strings[0]] + find_strings_with(strings[1:], target)
        else:
            return find_strings_with(strings[1:], target)

# Test find_strings_with
print("\nTest find_strings_with:")
result = find_strings_with(["hello", "world", "help", "test"], "hel")
print(f"  find_strings_with(['hello', 'world', 'help', 'test'], 'hel') = {result}")
print(f"  (expected: ['hello', 'help'])")
    
result = find_strings_with(["cat", "dog", "bird"], "z")
print(f"  find_strings_with(['cat', 'dog', 'bird'], 'z') = {result}")
print(f"  (expected: [])")

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    
    Time Complexity: O(n) where n is total number of files and directories
    Space Complexity: O(d) where d is maximum depth (recursion call stack)
    
    Recurrence Relation: T(n) = k + sum(T(child)) for each child directory
    This simplifies to O(n) since we visit each file/directory exactly once.
    """
    # Base case: if this path doesn't exist, return 0
    if not os.path.exists(directory_path):
        return 0
    
    # Base case: if this is a file (not a directory), return 1
    if os.path.isfile(directory_path):
        return 1
    
    # Recursive case: this is a directory
    # Count files in this directory and all subdirectories
    total_count = 0
    
    
    items = os.listdir(directory_path)
        
    for item in items:
        item_path = os.path.join(directory_path, item)
        # Recursive call: count files in subdirectory or count the file itself
        total_count += count_files(item_path)
    
    
    
    return total_count

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension.
    
    Time Complexity: O(n) where n is total number of files and directories
    Space Complexity: O(n*d) where n is matching files and d is depth
    """
    # Base case: if path doesn't exist
    if not os.path.exists(directory_path):
        return []
    
    # Base case: if this is a file
    if os.path.isfile(directory_path):
        # Check if it has the target extension
        if directory_path.endswith(extension):
            return [directory_path]
        else:
            return []
    
    # Recursive case: this is a directory
    infected = []
    
    items = os.listdir(directory_path)
        
    for item in items:
        item_path = os.path.join(directory_path, item)
        # Recursive call: find infected files in subdirectory or check this file
        infected.extend(find_infected_files(item_path, extension))
    
    
    return infected

# Alternative cleaner implementation:
def max_directory_depth(directory_path):
    """Cleaner version that's easier to understand."""
    if not os.path.exists(directory_path) or os.path.isfile(directory_path):
        return 0
    
    subdirs = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            subdirs.append(item_path)
    
    if not subdirs:
        return 0
    
    # Maximum depth among subdirectories, plus 1 for current level
    return 1 + max(max_directory_depth(subdir) for subdir in subdirs)


# Determine the time complexity of your solution



if __name__ == "__main__":
    print("")
    print("RECURSION ASSIGNMENT - STARTER CODE")
    print("Complete the functions above, then run this file to test your work.\n")
    
    # # Tests for count_files functions
    print("Total files (Test Case 1):", count_files("test_cases/case1_flat")) # 5
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested")) # 4
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected")) # 5
    # print("Total files (breeched files):", count_files("breach_data")) # ???

    # # Tests for find_infected_files function
    # print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case1_flat"))) # 0
    # print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case2_nested"))) # 0
    # print("Total Infected Files (Test Case 3):", len(find_infected_files("test_cases/case3_infected"))) # 3
    # print("Total Infected Files (breached files):", len(find_infected_files("breach_data"))) # ???

    ## Determine how many files were corrupted by department (Finance, HR, and Sales)
    # Call find infected files here

    
    print("\n⚠ Uncomment the test functions in the main block to run tests!")