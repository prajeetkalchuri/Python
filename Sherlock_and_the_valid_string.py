from collections import Counter
def isValid(s):
    dict = Counter(s)
    #case 01 same frequency 
    val = list(dict.values())
    if len(set(dict.values())) == 1:
        return "YES"
    #case 02 more than two unique frequencies 
    elif len(set(dict.values())) > 2:
        return "NO"
    #case03 two unique frequnecies 
    else:
        for key in dict :
            dict[key] -= 1
            temp = list(dict.values())
            #if we have zeroes in the list we have to remove that
            try :
                temp.remove(0)
            except:
                pass 
            
            if len(set(temp)) == 1:
                   return "YES"
            else :
                   dict[key] += 1
        return "NO" #means we can change all the characters to the same frequency 
    
    
    
s = input()
isValid(s) 
