# Solution for Assignment B
## Assumption
1. One number will only print one sentence e.g. 22 will only print 'Sentosa' once
## Logic for class Sentosa
1. Convert the number into **String** and use the **String** method `find` to look for the digit in the converted string.
2. It will return True if the digit can be found in the string, else return False.
3. Using the logical operators to create the required rules.
## Logic for class Sentosa_bitwise
1. Convert the number into a list of characters and using a recursive search function to look for the first occurence.
2. After looking for the first occurence, it will return 1 else it will return 0
3. By combining the bits, map it to a dictionary to print the correct rule
## Running the program / tests
```python3 solution_tests.py```