def odd_numbers(max_number):
    n = 1
    while n <= max_number:
        yield n
        n += 2
odd_numbers_15 = odd_numbers(15)
print(next(odd_numbers_15))
