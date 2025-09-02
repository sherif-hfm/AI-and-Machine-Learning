try:
    # Code that may raise an exception
    #result = 10 / 0
    result = 10 / 2
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
    print("Exception message:", e)
else:
    print("Division successful. Result:", result)
finally:
    print("Execution completed.")