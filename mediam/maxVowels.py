def maxVowels(string,k):
    maxLength=0
    vowels=['a','e','i','o','u']
    for i in range(len(string)-k+1):
        counter=0
        substring=string[i:i+k]
        for j in substring:
            if j in vowels:
                counter+=1
        maxLength=max(maxLength,counter)
    return maxLength

print(maxVowels("leetcode",2)) #3

def maxVowels2(string,k):
    vowels=set('aeiou')
    vowels_count=0
    maxCount=0
    for i in range(k):
        if string[i] in vowels:
             vowels_count+=1
    maxCount=max(maxCount,vowels_count)
    for i in range(k,len(string)):
        if string[i] in vowels:
            vowels_count+=1
        if string[i-k] in vowels:
            vowels_count-=1
        maxCount=max(maxCount,vowels_count)
    return maxCount


print(maxVowels2("leetcade",2))


