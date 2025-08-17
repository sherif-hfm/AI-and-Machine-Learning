def greet(name):
    return f"Hello {name}"

def square(num):
    return num * num

def sum_all(*numbers):
        total = 0
        for num in numbers:
            total += num
        return total

    

message = greet("Alice")
print(message)

result = square(4)
print(result)

print(sum_all(1, 2, 3))       