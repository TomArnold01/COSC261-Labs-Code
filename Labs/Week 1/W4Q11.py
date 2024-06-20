def shuffle(s,t):
    '''
        Define a Python 3 function shuffle(s, t) that returns the shuffle s||t of strings s and t. 
    Return the result as a set of strings, that is, without duplicates.'''

    result = []
    out = set()

    list_char_s = [*s]
    list_char_t = [*t]

    if len(list_char_s) == 0:
        for item in list_char_t:
            out.add(item)
        return out
    
    if len(list_char_t) == 0:
        for item in list_char_s:
            out.append(item)
        return out


    if len(list_char_s) == 1:
        result.append(list_char_s[0]+list_char_t[0])
        result.append(list_char_t[0]+list_char_s[0])
        return result
    
    for i in range(0,len(list_char_s)):
        result.append(shuffle(list_char_s[i], list_char_t[i]))

    holder = []
    for each in result:
        out.add(each[0]+each[1])
        for i in each:
            holder.append(i)

    test = 0
    for i in range((len(holder))-(len(holder)//2)):
        out.add(holder[i]+holder[i+2])
        out.add(holder[i]+holder[i+3-test])
        test += 2
           
    return out    
        





print(sorted(shuffle('ab', 'cd')))
# = ['abcd', 'acbd', 'acdb', 'cabd', 'cadb', 'cdab']
# print(sorted(shuffle('', 'e')))
# = ['e']