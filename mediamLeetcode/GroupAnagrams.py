def groupAnagram(words):

  #create a dictionary {}
  anagrams={}
  for word in range(len(words)):
    #sort the word 
    sortedWord=''.join(sorted(words[word]))
    if sortedWord in anagrams:
        anagrams[sortedWord].append(words[word])
    else:
       anagrams[sortedWord]=[words[word]]
  print(anagrams.values())

groupAnagram(["eat","tea","tan","ate","nat","bat"])