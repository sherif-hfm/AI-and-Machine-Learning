org_input = input("how many oranges : ")
amount = 5 - int(org_input)
print("You entered:", org_input)
print("Amount of oranges left:", amount)

# More type conversion examples
num_str = "123"
num_int = int(num_str)
print("String to int:", num_str, "->", num_int)

float_str = "45.67"
num_float = float(float_str)
print("String to float:", float_str, "->", num_float)

int_num = 10
str_num = str(int_num)
print("Int to string:", int_num, "->", str_num)

float_num = 3.1415
int_from_float = int(float_num)
print("Float to int (truncates):", float_num, "->", int_from_float)

bool_str_true = "True"
bool_str_false = "False"
print("String to bool (using eval):", bool_str_true, "->", eval(bool_str_true))
print("String to bool (using eval):", bool_str_false, "->", eval(bool_str_false))

zero = 0
nonzero = 42
print("Int to bool:", zero, "->", bool(zero))
print("Int to bool:", nonzero, "->", bool(nonzero))