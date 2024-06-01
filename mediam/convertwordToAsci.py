"""
we want to convert every string to its asci 
and increase asci by 5 and then return back the number 
as way of encoding 
ord function ms2olaa 3la convertion 
"""
def convertWordToAsci(word):
    encoded_chars=[]
    for char in word:
        encoded_char=chr(ord(char)+5)
        encoded_chars.append(encoded_char)
        encoded_string=''.join(encoded_chars)
    return encoded_string
print(convertWordToAsci('abcd')) 