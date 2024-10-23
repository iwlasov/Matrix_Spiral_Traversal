import aiohttp
import asyncio
from typing import List

async def get_matrix(url: str) -> List[int]:
    """
    функция получает текстовое представление матрицы по указанному URL
    возвращает список элементов матрицы который обошли по спирали
    против часовой стрелки, начиная с левого верхнего угла
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if ((response.status >= 500) or (response.status != 200)):
                    raise Exception(f'HTTP error: {response.status}')

                matrix_text = await response.text()
                print('текстовое представление матрицы:\n', matrix_text)
                matrix = format_matrix(matrix_text)
                return traverse_matrix_spiral(matrix)

        except aiohttp.ClientError as e:
            raise Exception(f'Network ClientError: {e}')
        except asyncio.TimeoutError:
            raise Exception('Request TimeoutError')
        

def format_matrix(matrix_text: str) -> List[List[int]]:
    """
    функция преобразует текстовое представление матрицы в двумерный список целых чисел
    """
    text = matrix_text.strip().split('\n')

    result = []
    for i in range(1, len(text), 2):
        result.append(list(map(lambda x: int(x.strip()), text[i].strip('| ').split('|'))))

    print('двумерный список целых чисел:\n', result)
    return result

def traverse_matrix_spiral(matrix: List[List[int]]) -> List[int]:
    """
    функция обхода матрицы по спирали против часовой стрелки, начиная с левого верхнего угла.
    """
    result = []
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix) if matrix else 0

    while top < bottom and left < right:
        # Сверху вниз по левому столбцу
        for i in range(top, bottom):
            result.append(matrix[i][left])
        left += 1
        # Слева направо по нижней строке
        for i in range(left, right):
            result.append(matrix[bottom - 1][i])
        bottom -= 1

        if left < right:
            # Снизу вверх по правому столбцу
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][right - 1])
            right -= 1

        if top < bottom:
            # Справа налево по верхней строке
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[top][i])
            top += 1

    print('список элементов матрицы по спирали:\n', result)
    return result
    