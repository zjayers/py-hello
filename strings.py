# Multi Lines
mult_lines = '''
Multiple
Lines
'''

# Formatted Strings
first = "Zach"
last = 'Ayers'
print(f"{first} {last}")

#  Useful String Methods
print(len(first))  # Get String Length
print(first.upper())  # To Upper Case
print(first.lower())  # To Lower Case
print(first.title())  # To Title Case
print(first.strip())  # Remove Whitespace
print(first.lstrip())  # Remove Left Whitespace
print(first.rstrip())  # Remove Right Whitespace
print(first.find("ch"))  # Find index in string
print(first.replace("Z", "-"))  # Replace char in string
print("Zach" in first)  # Check if chars in string
print("Zach" not in first)  # Check if chars not in string
