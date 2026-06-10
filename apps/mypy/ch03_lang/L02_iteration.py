def main():
    print("Python Iteration Demo")
    while True:
        name = input("What is your name? ")
        if not name:
            break

        print(f"Nice to meet you, {name}!")

    nums = [ 1, 5, 8, 10, 7, 2 ] # <--- List<object>
    for i in nums:
        print(f"The next number is {i}")
    # this is the equivalent of foreach in C#

    # There is NO equivalent of
    # for (i-0; i < len(nums); i++)
    # In Python, use tuple
    for idx,num in enumerate(nums):
        print(f"The {idx}th number is {num}")
    print()

    for idx,num in enumerate(nums, start=1): #<-- variation
        print(f"The {idx}th number is {num}")
    print()

    # Python support for range
    for n in range(1, 6): #<-- prints 5 times
        print("Print me")
    print()

    for _ in range(1, 6): # when n is not used in the block
        print("Print me")

if __name__ == '__main__':
    main()