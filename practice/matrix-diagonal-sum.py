class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def diagonalSum(self):
        """
        Calculate diagonal sums of primary and secondary diagonals. The repeating numbers are excluded.
        """
        count_row = len(self.matrix)
        count_column = len(self.matrix[0])
        j = count_row
        total = 0
        in_primary_diagonal = []
        for i in range(0, count_column):
            if (self.matrix[i][count_row - j] == self.matrix[i][j - 1]) and self.matrix[i][
                count_row - j] not in in_primary_diagonal:
                total = total + self.matrix[i][count_row - j]
            else:
                total = total + self.matrix[i][count_row - j] + self.matrix[i][j - 1]
            j = j - 1
        return total


input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = Matrix(input_matrix)
print(matrix.diagonalSum())
