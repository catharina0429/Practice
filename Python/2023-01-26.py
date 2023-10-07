def is_ascending(items: list[int]) -> bool:
    # your code here
    return sorted(list(set(items))) == items

print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

# print(sorted(list([1,1,1,1])) == list([1,1,1,1]))
# print(list(set([1,3,3,5])) == list([1,3,3,5]))