# 부분 정답

num_A, num_B = input().split()
numbers = "0123456789abcdefghijklmnopqrstuvwxyz"
possible = []

for i in range(36):  # A진법
    for j in range(36):  # B진법
        ten_A = 0
        ten_B = 0
        A_idx_reverse = -1
        B_idx_reverse = -1

        for A_idx in range(len(num_A)):
            ten_A += (i ** A_idx) * int(numbers.index(num_A[A_idx_reverse]))
            A_idx_reverse -= 1

        for B_idx in range(len(num_B)):
            ten_B += (j ** B_idx) * int(numbers.index(num_B[B_idx_reverse]))
            B_idx_reverse -= 1

        if i != j and ten_A == ten_B:
            possible.append([ten_A, i, j])

# print(possible)
if len(possible) == 0 or possible[0][0] >= 2 ** 63:
    print("Impossible")
elif len(possible) >= 2:
    print("Multiple")
else:
    print(str(possible[0][0]) + " " + str(possible[0][1]) + " " + str(possible[0][2]))
