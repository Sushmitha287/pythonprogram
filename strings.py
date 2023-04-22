#methods in strings:
#len()
#in,not in
#rstrip()
#lstrip()-to remove blank spaces
#strip()
s="abcdefg"
#s.find(substring)-Returns index of first occurrence of the given substring. If it is not available then we will get -1.
#s.find(substring,beg,end)
#s.rfind()-backward
#s.index()-same as find(),not found get an error
#s.rindex()
#s.count(substr)
#s.count(substr,beg,end)
#s.replace(oldstring,newstring)
#s.split(seperator, Maximum splits),rsplit()=gives list
#s=seperator.join(group of strings)
Changing case of the string:
#upper()-To convert all characters to upper case
#lower()-To convert all characters to lower case
#swapcase()-converts all lower case characters to upper case and all upper case characters to lower case
#title()-To convert all characters to title case. i.e., first character in every word should be upper case and all remaining characters should be in lower case.
#capitalize()-Only first character will be converted to upper case and all remaining characters can be converted to lower case.
#s.startswith(substring)
#s.endswith(substring)
checking type of character:
#isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
#isalpha(): Returns True if all characters are only alphabet symbols(a to z , A to Z)
#isdigit(): Returns True if all characters are digits only( 0 to 9)
#islower(): Returns True if all characters are lower case alphabet symbols
#isupper(): Returns True if all characters are upper case alphabet symbols
#istitle(): Returns True if string is in title case
#isspace(): Returns True if string contains only spaces
#format()
