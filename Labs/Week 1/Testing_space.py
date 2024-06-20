def all_subsets(s):
    if len(s) == 0:
        return [set()]
    
    element = s.pop()
    subsets = all_subsets(s)
    new_subsets = [subset.union({element}) for subset in subsets]
    
    return subsets + new_subsets





print(sorted(map(sorted, all_subsets({0, 1, 2}))))
# # [[], [0], [0, 1], [0, 1, 2], [0, 2], [1], [1, 2], [2]]

# print(sorted(map(sorted, all_subsets({'a', 'b'}))))
# # [[], ['a'], ['a', 'b'], ['b']]

# print({1} in all_subsets({0, 1, 2}))
# #  True