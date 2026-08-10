def minimax(depth, node, maxTurn, values, height):
    if depth == height:
        return values[node]

    if maxTurn:
        return max(minimax(depth+1, node*2, False, values, height),
                   minimax(depth+1, node*2+1, False, values, height))
    else:
        return min(minimax(depth+1, node*2, True, values, height),
                   minimax(depth+1, node*2+1, True, values, height))

values = [3, 5, 2, 9, 12, 5, 23, 23]
height = 3

print("Best value:", minimax(0, 0, True, values, height))
