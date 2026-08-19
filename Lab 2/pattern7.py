n = 4

for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        
        row = abs(n - i)
        col = abs(n - j)
        
        print(max(row, col) + 1, end=" ")
    
    print()