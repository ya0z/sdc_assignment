###
# Title: Assignment B Solution
# Description: Solution for Assignment B
# Author: Lu Yaomin
#
# History:
# 20210325 - v1.0: Using function find in string module to search for the characters 2 and 7
# 20210325 - v1.1: Create another class with a bitwise search function
###
class Sentosa:
    def __init__(self):
        print('Class Sentosa initiated')

    def find_num(self, text, lookup):
        # If the character is not found, the find function will return -1 instead of returning the index of the character found in the string
        if (text.find(lookup) == -1):
            return False
        else:
            return True

    def print_num(self, num):
        # Convert the number to string and pass to find_num function
        found_two = self.find_num(str(num),'2')
        found_seven = self.find_num(str(num),'7')
        # Logical operations to print the correct string according to the rules
        if (found_two and not(found_two and found_seven)):
            print('Sentosa')
        elif (found_seven and not(found_two and found_seven)):
            print('State of Fun')
        elif (found_two and found_seven):
            print('Sentosa - State of Fun')
        else:
            print(num)

class Sentosa_bitwise:
    def __init__(self):
        print('Class Sentosa_bitwise initiated')

    def find_num(self, lst, num):
        # Look at the first character in the list and see if match
        if (lst[0] == num):
            return 1
        elif (len(lst) == 1):
            return 0
        # Continue to look for the character in the list
        return self.find_num(lst[1:], num)

    def print_num(self, num):
        lst = [str(i) for i in str(num)]
        found_two = self.find_num(lst, '2')
        found_seven = self.find_num(lst, '7')
        
        # Combine the two bits and map to the dictionary
        bitwise = str(found_two) + str(found_seven)
        bitwise_map = {
                '10' : 'Sentosa',
                '01' : 'State of Fun',
                '11' : 'Sentosa - State of Fun',
                '00' : num
        }
        print(bitwise_map.get(bitwise, num))

