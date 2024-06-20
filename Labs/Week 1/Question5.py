def all_strings(alpha, length):
    holder = []
    result = []
    iterations = 0

    if length == 0:
        result.append('')
        iterations = length-1
        

    if length == 1:
        for item in alpha:
            result.append(str(item))

    while iterations != length-1:
        
        for each in alpha:
            if iterations == 0:
                for test in alpha:
                    holder.append(str(each) + str(test))
            else: 
                for entry in holder:
                    result.append(str(entry) + str(each))
        iterations += 1
        
        if iterations >= 2:
            if iterations != length-1:
                placeholder = result
                holder = placeholder
                result = []

    if iterations == 1:
        return holder
    else:
        return result
    
        

# print(sorted(all_strings({0, 1}, 0)))

# ['000', '001', '010', '011', '100', '101', '110', '111']

# print(sorted(all_strings({'a', 'b'}, 2)))

print(len(all_strings({'a', 'b', 'c'}, 2)))