# Built-In Python Features

## Length of a String
text = "Python Is Very Easy"
length = len(text)
print("Length of text: ", length)

## Upper and Lower Case
upper = text.upper()
lower = text.lower()
print("Upper case: ", upper)
print("Lower case: ", lower)

## Replace
og_text = "We are learning Python for DevOps"
new_text = og_text.replace("Python", "Linux")

print("Original text: ", og_text)
print("New text: ", new_text)

## Split
split = og_text.split(" ")
print("Splitting og_text into Words: ", split)
print("Third word (after split): ", split[2])

arn = "arn:partition:service:region:account-id:resource-type/resource-id"
split_arn = arn.split("/")
print("Original arn: ", arn)
print("Splitting arn into two parts: ", split_arn)
print("First part of arn (after split): ", split_arn[0])
print("Second part: resource-id (after split): ", split_arn[1])


