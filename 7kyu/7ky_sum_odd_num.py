class Triangle:

    def __init__(self, number):
        self.number = number

    def sum_triangle(self):
        triangle = [i for i in range(self.number ** 2 + self.number) if i % 2 != 0]
        return sum(triangle[len(triangle) - self.number:])


def row_sum_odd_numbers(n):
    triangle = Triangle(n)
    return triangle.sum_triangle()


num = row_sum_odd_numbers(3)
print(num)
