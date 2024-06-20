





        
def all_strings(alpha, length):
    if length == 0:
        return ['']
    
    result = []
    for string in all_strings(alpha, length - 1):
        for symbol in alpha:
            result.append(string + str(symbol))
    return result
        








print(len(all_strings({1,2,3,4,5,6,7,8}, 1)))
print(len(all_strings({1,2,3,4,5,6,7,8}, 2)))
print(len(all_strings({1,2,3,4,5,6,7,8}, 3)))