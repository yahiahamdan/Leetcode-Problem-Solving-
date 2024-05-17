"""
lets  review what is tuple and what is used for 
tuple zey list bs immutable can't be updated 
() 
ordered 3ady zey list but we cant remove elements of tuple once created 
"""
def UniqueList(lists):
    uniq_dict={tuple(item):item for item in lists}
    uniqList=list(uniq_dict.values())
    print(uniqList)

lists = [[1, 1], [3, 4], [1, 2], [5, 6], [3, 4]]
print(UniqueList(lists))

"""
y3ny approach ely anan 3mlto dh by5ly sublist deh tkoon set 
sublist tkoon set no set inside a set 
lw gbt set(set) will give me error
sets mmkn t3dhla 3ady we fe nfs wa2t mmkn tzbtha  
tuple()item uniquelist 
"""