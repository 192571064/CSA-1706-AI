def alphabeta(d, node, alpha, beta, maxTurn, values, h):
    if d == h:
        return values[node]

    if maxTurn:
        best = -999
        for i in [node*2, node*2+1]:
            best = max(best, alphabeta(d+1, i, alpha, beta, False, values, h))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = 999
        for i in [node*2, node*2+1]:
            best = min(best, alphabeta(d+1, i, alpha, beta, True, values, h))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 2, 9, 12, 5, 23, 23]
h = 3

print("Best value:", alphabeta(0, 0, -999, 999, True, values, h))
