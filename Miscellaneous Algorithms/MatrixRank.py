def swap(mat,row1,row2,col):
    for i in range(col):
        temp = mat[row1][i]
        mat[row1][i] = mat[row2][i]
        mat[row2][i] = temp

def rankOfMatrix(mat,C,R):
    rank = C
    for row in range(rank):
        if mat[row][row]!=0 :
            for col in range(R):
                if col != row :
                    mult = mat[col][row] /mat[row][row]
                    for i in range(rank):
                        mat[col][i] = mat[col][i] - mult * mat[row][i]
        else :
            reducemat = true
            for i range(row+1,R):
                if mat[i][row] !=0:
                    swap(mat, row, i, rank)
                    reducemat = false
                    break
            if reducemat == true :
                rank=rank-1
                for i in range(R):
                    mat[i][row] = mat[i][rank]
            row=row-1;
    return rank;
R=input("No. of Rows")
C=input("Np. of Columns")
mat=[[0]*C for i range(R)]
print "Enter Matrix Elements"
for i in range(R):
    for j in range(C):
        mat[i][j]=input()

print "Rank of MAtrix", rankOfMatrix(mat,C,R)
