# Initial State
a = [[1,2,3],
     [5,0,6],
     [4,7,8]]

# Goal State
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

print("Initial State")
for i in a:
    print(i)

while a != goal:

    # Find blank position
    for i in range(3):
        for j in range(3):
            if a[i][j] == 0:
                br = i
                bc = j

    print("\nBlank Position :", br, bc)

    # Find required value from goal state
    value = goal[br][bc]

    print("Required Value :", value)

    # Find that value in current state
    for i in range(3):
        for j in range(3):
            if a[i][j] == value:
                vr = i
                vc = j

    print("Value Found At :", vr, vc)

    # Swap
    a[br][bc], a[vr][vc] = a[vr][vc], a[br][bc]

    print("\nCurrent State")
    for i in a:
        print(i)

print("\nGoal State Reached")
