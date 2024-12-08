## Вопрос №1
#### Условие:
На языке Python или C++ написать алгоритм (функцию) определения четности целого числа,  
который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.  
Объяснить плюсы и минусы обеих реализаций.  
Пример:  
	![[Pasted image 20241208194310.png]]
#### Комментарии:
Проверка на чётность с помощью побитового И
    ![[Pasted image 20241208190434.png]]
    Плюсы: быстра, проще некуда для процессора 
	Минусы: менее универсальна; может быть непонятна для совсем новичков
## Вопрос №2
#### Условие:
На языке Python или С++ написать минимум по 2 класса реализовывающих циклический буфер _data.  
Объяснить плюсы и минусы каждой реализации.  
  
Оценивается:  
  
Полнота и качество реализации  
Оформление кода  
Наличие сравнения и пояснения по быстродействию
#### Комментарии:
Первая реализация чуть сложнее и в теории быстрее, вторая настолько проста, насколько возможна, но требует чуть больше памяти и в теории медленнее.
## Вопрос №3
#### Условие:
На языке Python или C++ предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.  
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).  
Объяснить, почему вы считаете, что функция соответствует заданным критериям.
#### Комментарии:
Сортировка слиянием обладает небольшой алгоритмической сложностью, эффективна, проста и стабильна. Изначально планировал расписать Timsort, но получилось довольно громоздко, так что в итоге отказался.