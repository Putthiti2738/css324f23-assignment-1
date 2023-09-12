def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    Capacity = (8, 5, 3)
    Action = []
    for i in range(3):
        for j in range(3):
            if i != j:
                Amount = min(x[i], capacities[j] - x[j])
                State = list(x)
                State[i] -= Amount
                State[j] += Amount
                Action.append((tuple(State), Amount))
    return Action
