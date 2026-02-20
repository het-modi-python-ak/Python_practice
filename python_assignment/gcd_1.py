# Dictionary to map words to digits
wrdtodigi = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

digitowrd = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

# Convert word string to number
def wordtonum(word_string):
    result = ""
    temp = ""
    i = 0
    
    while i < len(word_string):
        temp += word_string[i]
        if temp in wrdtodigi:
            result += wrdtodigi[temp]
            temp = ""
        i += 1
    
    if temp != "":  
        return None
    
    return int(result)


def numtowrd(number):
    number_str = str(number)
    result = ""
    i = 0
    
    while i < len(number_str):
        result += digitowrd[number_str[i]]
        i += 1
    
    return result



def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)



try:
    input1 = input("Input 1: ").strip().lower()
    input2 = input("Input 2: ").strip().lower()
    
    num1 = wordtonum(input1)
    num2 = wordtonum(input2)
    
    if num1 is None or num2 is None:
        print("Invalid Input")
    else:
        
       
        
        result = gcd(num1, num2)
        print("Output:", numtowrd(result))

except Exception:
    print("Invalid Input")