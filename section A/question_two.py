def odd_numbers():
    integers = [2,4,7,9,12,15]
    sum = 0
    for i in integers:
        if i % 2 != 0:
            sum += i
    print(f"The sum of all odd numbers in the list of integers is: {sum}")
odd_numbers()