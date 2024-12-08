'''
Вопрос №3

На языке Python или C++ предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
Объяснить, почему вы считаете, что функция соответствует заданным критериям.
'''

'''
Вообще я хотел тут расписать Timsort, но её полноценная реализация достаточно громоздкая, так что решил 
оставить менее эффективную, но всё ещё быструю, стабильную и простую сортировку слиянием.
'''
from typing import Iterable


def merge_sort(arr: Iterable):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1
