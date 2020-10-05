
def linear_evolve(B, v):
    new_state = []
    for op in B:
        partial_state = 0
        for idx in range(len(op)):
            partial_state+=op[idx]*v[idx]
        new_state.append(partial_state)

    return new_state
