# STRING
A = "Hello"
B = "World"
text = "Python is very easy"
length = len(text)

result = A + " " + B
print("String concatenation: ", result)
print("Length of text: ", length)

# INTEGER
num1 = 20
num2 = 10

addition = num1 + num2
print("Integer addition: ", addition)

div = num1 // num2
print("Integer division: ", div)

ren = num1 % num2
print("Integer remainder: ", ren)

# FLOAT
f1 = 5.0
f2 = 2.5

additionf = f1 + f2
print("Float addition: ", additionf)

substractionf = f1 - f2
print("Float substraction: ", substractionf)

multiplicationf = f1 * f2
print("Float multiplication: ", multiplicationf)

divisionf = f1 / f2
print("Float division: ", divisionf)

# LIST
my_list = [1,2,3,4,5,6,7]
serversIP = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

print("My List: ", my_list)
print("List of Servers IP: ", serversIP)

my_list[0] = 10
print("Modified My List: ", my_list)

## LIST APPEND
serversIP.append("192.168.1.4")
print("List of Servers IP after append: ", serversIP)

# TUPLES
my_tuple = (1,2,3,4,5,6,7)
print("My Tuple: ", my_tuple)

## Not posible to modify a tuple because it is immutable
## my_tuple[0] = 10
## print("Modified My Tuple: ", my_tuple)

# SETS
## Useful for unique values, than means avoids duplicates of server IPs, Security Groups, etc
my_sets = {1,2,3,4,5,6,7}
print("My Set: ", my_sets)

my_sets.add(8)
print("My Set after add: ", my_sets)

# DICTIONARY
employee = {
    "name": "John Doe",
    "age": 30,
    "position": "Software Engineer",
    "salary": 9000
}

print("Employee Name: ", employee["name"])

## To add new Key-Value pair
employee["department"] = "IT"
print("Employee after adding department: ", employee)

## Update existing Key-Value pair
employee["salary"] = 9500
print("Employee salary after updating salary: ", employee["salary"])

# BOOLEAN
is_server_up = True
if is_server_up:
  print("The server is running!")
else:
  print("The server is Down!")