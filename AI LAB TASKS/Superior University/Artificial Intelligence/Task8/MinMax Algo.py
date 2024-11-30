def MiniMax(curr_state, node_i, maxTurn, total, goal_state):
    if curr_state == goal_state:
        return total[node_i]
    if maxTurn:
        return max(
            MiniMax(curr_state + 1, node_i * 2, False, total, goal_state),
            MiniMax(curr_state + 1, node_i * 2 + 1, False, total, goal_state)
        )
    else:
        return min(
            MiniMax(curr_state + 1, node_i * 2, True, total, goal_state),
            MiniMax(curr_state + 1, node_i * 2 + 1, True, total, goal_state)
        )
total = [67, 54, 22, 8, 34, 22, 2, 43]
treeDepth = 0
n = len(total)
while n > 1:
    n //= 2
    treeDepth += 1
print(MiniMax(0, 0, True, total, treeDepth))

