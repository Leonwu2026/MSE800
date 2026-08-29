# Develop a Python OOP project that accepts two matrices as 2D lists and multiplies them together 
# (e.g., M1 size: 3*5 - M2 size: 5*2). Share your complete code here.


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def multiply(self, other):
        # 第一个矩阵的列数必须等于第二个矩阵的行数
        if self.columns != other.rows:
            raise ValueError(
                "Matrix multiplication is not possible: "
                "the columns of matrix 1 must equal the rows of matrix 2."
            )

        result = []

        # 遍历第一个矩阵的每一行
        for i in range(self.rows):
            new_row = []

            # 遍历第二个矩阵的每一列
            for j in range(other.columns):
                total = 0

                # 第一个矩阵的行 × 第二个矩阵的列
                for k in range(self.columns):
                    total += self.data[i][k] * other.data[k][j]

                new_row.append(total)

            result.append(new_row)

        return Matrix(result)

    def display(self):
        for row in self.data:
            print(row)


def main():
    matrix1_data = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    matrix2_data = [
        [10, 11],
        [20, 21],
        [30, 31]
    ]

    matrix1 = Matrix(matrix1_data)
    matrix2 = Matrix(matrix2_data)

    matrix3 = matrix1.multiply(matrix2)

    print("Matrix 1:")
    matrix1.display()

    print("\nMatrix 2:")
    matrix2.display()

    print("\nMatrix 1 × Matrix 2:")
    matrix3.display()


if __name__ == "__main__":
    main()