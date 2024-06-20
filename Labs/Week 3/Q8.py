def epsilon_closure(state, nfa):
    epsilon_states = set()  
    stack = [state]  

    while stack:
        current_state = stack.pop()
        epsilon_states.add(current_state) 

        if "_" in nfa[current_state]:
            epsilon_transitions = nfa[current_state]["_"]
            for next in epsilon_transitions:
                if next not in epsilon_states:
                    stack.append(next)  

    return epsilon_states
# NFA with multiple epsilon transitions from the same state
multi_transition_nfa = {
       0: {"_": {2, 1}, "a": {1}, "b": {2}},
       1: {"a": {1}, "b": {0}},
       2: {"_": {3, 1}, "a": {1}, "b": {2}},
       3: {"a": {2}}
      }
for i in range(4):
    print(f"Epsilon closure for q{i}: {sorted(epsilon_closure(i, multi_transition_nfa))}")