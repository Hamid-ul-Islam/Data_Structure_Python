def fib(n: int):
        if n <= 1:
            return n

        def matrix_multiply(a, b):
            return [
                [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
            ]

        def matrix_power(matrix, exp):
            result = [[1, 0], [0, 1]]
            while exp:
                if exp % 2:
                    result = matrix_multiply(result, matrix)
                matrix = matrix_multiply(matrix, matrix)
                exp //= 2
            return result

        base_matrix = [[1, 1], [1, 0]]
        result_matrix = matrix_power(base_matrix, n - 1)

        return result_matrix[0][0]


print(fib(1000))