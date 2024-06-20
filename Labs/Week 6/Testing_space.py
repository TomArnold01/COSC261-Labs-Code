def cfg_str_to_dict(cfg_str):
    """Converts a multiline CFG string representation 
       of the form used in COSC261 quiz questions 
       into a dictionary represention, e.g.
       "S=ab|bA|BB|_" becomes {"S": ["ab", "bA", "BB", ""]}
    """
    nonterminals = {char for char in cfg_str if char.isupper()}.union({'S'})
    result = {nt: [] for nt in nonterminals}
    productions = cfg_str.splitlines()
    for production in productions:
        nt, rhs = production.split("=")
        rhs = rhs.replace("_", "") # Use "" for epsilon
        rhs_list = rhs.split("|")
        result[nt] = result[nt] + rhs_list
    return result

def generating_nts(cfg_str):
    cfg_dict = cfg_str_to_dict(cfg_str)
    find_non_genterating(cfg_dict)
    master_cfg_keys = cfg_str_to_dict(cfg_str).keys()
    cfg_dict_keys = cfg_dict.keys()
    result = []
    for items in master_cfg_keys:
        add = True
        for i in cfg_dict_keys:
            if i == items:
                add = False
        if add == True:
            result.append(items)
    if len(result) != 0:
        return set(result)
    else:
        return set()

def find_non_genterating(cfg_dict):
    keys = cfg_dict.keys()
    result = dict()
    for item in keys:
        for each in cfg_dict.get(item):    
            if each.islower() or each == '' or each.isnumeric(): #epsilon dipshit
                result.update({item:each})
                break
    if len(result) == 0:
        return         
    for i in result:
        cfg_dict.pop(i)  
        change(i, result.get(i), cfg_dict)
    find_non_genterating(cfg_dict)
    

def change(to_change, char, cfg_dict):
    if char == '' or char.isnumeric():
        char = 'p' # is p comes up it means that it has delt with  

    keys = cfg_dict.keys()
    for item in keys:
        changed = False 
        for i, each in enumerate(cfg_dict.get(item)):
            
            new_string = change_string(each, to_change, char)
            if new_string != each:  
                cfg_dict[item][i] = new_string
                changed = True
        if not changed:
            cfg_dict[item] = cfg_dict.get(item)

def change_string(string, to_change, char):
    new_string = ''
    for letter in string:
        if letter == to_change:
            new_string += char
        else:
            new_string += letter
    return new_string

	
# A and C are not generating. Can you see why?
cfg = """S=aAa|bBb
A=aC|bAA
B=b|aBB
C=Ab|bA"""
print(sorted(generating_nts(cfg)))