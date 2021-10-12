def concatenetedString(s1,s2):
    
    res = "" # result 
    m = {}
      
    # store all characters of s2 in map /dict 
    for i in range(0, len(s2)):
        m[s2[i]] = 1
        #print(m)
  
    # Find characters of s1 that are not 
    # present in s2 and append to result 
    for i in range(0, len(s1)):
        if(not s1[i] in m):
            res = res + s1[i]
        else:
            m[s1[i]] = 2
        #print(m)
  
    # Find characters of s2 that are not 
    # present in s1.         
    for i in range(0, len(s2)):
        if(m[s2[i]] == 1):
            res = res + s2[i]
        #print(m)
  
    return res     
      
# Driver Code
if __name__ == "__main__":
    s1 = "abcs"
    s2 = "cxzca"
    print(concatenetedString(s1, s2))
    
    
    
 #2nd Approach
"""
def concat(s1,s2):
    
    st1 = set(s1)
    #print(st1)
    st2 = set(s2)
    #print(st2)
    s = list(st1 & st2)
    #print(s)
    a = [i for i in s1 if i not in s]
    b = [i for i in s2 if i not in s]
    print(a)
    print(b)
    finalstring = a + b
    #print(finalstring)
    return ''.join(finalstring)
    
    
s1 = "abcs"
s2 = "cxzca"
print(concat(s1,s2))
"""
