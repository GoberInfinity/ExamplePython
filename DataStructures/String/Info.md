# UTF8 Strings

You can reverse a utf8 string the problem is that does the reversal make sense and does it conform to language and cultural rules, characters, and encoding.

Unicode is a character set. UTF-8 is encoding.

Unicode is a list of characters with unique decimal numbers (code points). A = 65, B = 66, C = 67, ....
This list of decimal numbers represent the string "hello": 104 101 108 108 111

Encoding is how these numbers are translated into binary numbers to be stored in a computer:
UTF-8 encoding will store "hello" like this (binary): 01101000 01100101 01101100 01101100 01101111
