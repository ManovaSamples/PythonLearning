def most_frequent(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    max_count = 0
    most_frequent_number = None
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            most_frequent_number = number
    return most_frequent_number

print(most_frequent([1, 2, 3, 3, 3, 4, 5, 5,5]))