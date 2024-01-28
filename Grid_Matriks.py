#2D LIST
grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#mencari nilai kolom 2 dan baris 3
print(grid[1][2])
#mencari nilai kolom 3 dan baris 2
print(grid[2][1])

#loop grid
for row in grid:
    print(row)
#mencetak matriks

#grid value
for row in grid:
    for col in row:
        print(col)
#mencetak semua elemen value di grid