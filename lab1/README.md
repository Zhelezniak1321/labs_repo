## Лабораторні роботи з дисципліни "Алгоритмізація та програмування частина 2"
## Виконав: Железняк Олександр Степанович(ІР-13)
## Лабораторна робота №1 (Варіант 2) Рівень 2

### Завдання:
Масив вважається монотонним, якщо всі його елементи розташовані в зростаючому або
спадаючому порядку.
Завдання: Напишіть функцію, яка перевіряє, чи є заданий масив монотонним. Функція
повинна повертати логічне значення True, якщо масив є монотонним, і False, якщо масив не є
монотонним.
Приклад вхідних даних і результатів:
1. Для масиву [1, 2, 3, 4, 5] функція повертає True, оскільки всі елементи зростають
монотонно.
2. Для масиву [5, 4, 3, 2, 1] функція повертає True, оскільки всі елементи спадають
монотонно.
3. Для масиву [1, 2, 2, 3, 2, 4] функція повертає False, оскільки масив не є строго
монотонним.
Зверніть увагу, що масив із однаковими значеннями наступного елемента вважається
монотонним.
Для перевірки виконання роботи реалізованого алгоритму слід використати
бібліотеку unittest .