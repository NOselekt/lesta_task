'''
Вопрос №2

На языке Python или С++ написать минимум по 2 класса реализовывающих циклический буфер _data.
Объяснить плюсы и минусы каждой реализации.

Оценивается:

Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
'''

class RingBuffer1():
    '''
    Первый способ реализовать кольцевой буфер.
    Плюсы: в теории быстрее и использует меньше памяти
    Минусы: сложнее
    '''
    def __init__(self, size):
        '''
        Инициализирует буфер.
        :param size: размер буфера.
        _data: список, в котором будут храниться данные.
        '''
        self.size = size
        self._data = []
        self._current = 0


    def append(self,element):
        '''
        Добавление элемента в буфер.
        :param element: новый элемент.
        :return: None
        '''
        if len(self._data) == self.size:
            self._data[self._current] = element
            self._current = (self._current + 1) % self.size
            return None
        self._data.append(element)

    def pop_eldest(self):
        '''
        Получение и удаление самого старого элемента.
        :return: самый старый элемент буфера.
        '''
        if self._data:
            result = self._data.pop(self._current)
            if self._current >= len(self._data):
                self._current -= 1
            return result

    def get_eldest(self):
        '''
        Получение самого старого элемента без удаления.
        :return: самый старый элемент буфера.
        '''
        return self._data[self._current] if self._data else None

    def get(self):
        '''
        Получение всех данных из буфера.
        :return: список всех элементов в буфере.
        '''
        return self._data

class RingBuffer2():
    '''
    Второй способ реализовать кольцевой буфер.
    Плюсы: самая простая и очевидная реализация
    Минусы: в теории медленнее и требует чуть больше памяти
    '''
    def __init__(self, size):
        self.size = size
        self.__data = []

    def append(self, element):
        '''
        Добавление элемента в буфер.
        :param element: новый элемент.
        :return: None
        '''
        self.__data.append(element)
        if len(self.__data) == self.size:
            self.__data.pop(0)
        return None

    def pop_eldest(self):
        '''
        Получение и удаление самого старого элемента.
        :return: самый старый элемент буфера.
        '''
        return self._data.pop(0) if self._data else None

    def get_eldest(self):
        '''
        Получение самого старого элемента без удаления.
        :return: самый старый элемент буфера.
        '''
        return self._data[0] if self._data else None

    def get(self):
        '''
        Получение всех данных из буфера.
        :return: список всех элементов в буфере.
        '''
        return self._data
