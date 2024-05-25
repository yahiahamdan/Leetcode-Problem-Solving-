def groupAnagram(words):

  #updating the probelem of group anagrams
  anagrams={}
  for word in range(len(words)):
    #sort the word 
    sortedWord=''.join(sorted(words[word]))
    if sortedWord in anagrams:
        anagrams[sortedWord].append(words[word])
    else:
       anagrams[sortedWord]=[words[word]]
  return list(anagrams.values())

groupAnagram(["eat","tea","tan","ate","nat","bat"])