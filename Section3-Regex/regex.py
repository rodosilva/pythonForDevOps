# Import Regular Expression module
import re

# Variables
text = "Hello World"
pattern = r"World" # Raw string for regex pattern

# Results of Regex operations
## Match
resultM = re.match(pattern, text) # Match pattern at the start of the string

print("Match at the beginning of the string: ", resultM)

## Search
resultS = re.search(pattern, text) # Search for pattern anywhere in the string (But shows only the first match)
if resultS:
  print("Search anywhere in the string: ", resultS.group())

## Find All
text2 = "Hello all, how are you? \
     My name is Rodrigo and I am learning Python. \
    I hope to learn Python as fast as I can."

patternFA = r"Python"

resultFA = re.findall(patternFA, text2) # Find all occurrences of the pattern in the string
print("Find all occurrences of the pattern: ", resultFA)

## Sub
text3 = "Hello      all, how     are you?    "
patternSub = r"\s+" # Pattern to match one or more whitespace characters
resultSub = re.sub(patternSub, " ", text3) # Replace multiple spaces with a single space
print("Substituted multiple spaces: ", resultSub)
