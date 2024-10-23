import asyncio
from matrix_spiral import get_matrix, traverse_matrix_spiral

# URL-адрес, по которому находится текстовое представление матрицы
SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'

# Ожидаемый результат обхода матрицы по спирали
TRAVERSAL = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]

def test_get_matrix():
    """
    Тестируем функцию get_matrix.
    """
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL

def test_traverse_matrix_spiral():
    """
    Тестируем функцию traverse_matrix_spiral на матрице 5х5.
    """
    SOURCE = [[10,  20,  30,  40,  50],
              [60,  70,  80,  90,  100],
              [110, 120, 130, 140, 150],
              [160, 170, 180, 190, 200],
              [210, 220, 230, 240, 250]]
    TRAVERSAL = [10, 60, 110, 160, 210, 220, 230, 240, 250, 200, 150, 100, 50, 40, 30, 20, 70, 120, 170, 180, 190, 140, 90, 80, 130]

    assert traverse_matrix_spiral(SOURCE) == TRAVERSAL

if __name__ == "__main__":

    # Запускаем тесты
    test_get_matrix()
    test_traverse_matrix_spiral()

    print("Тесты пройдены")
