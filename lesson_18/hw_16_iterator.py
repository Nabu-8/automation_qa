# Ітератори:
#     Реалізуйте ітератор для зворотного виведення елементів списку.
class ReversedListElements:
    def __init__(self, el_list):
        if not isinstance(el_list, list):
            raise TypeError("Input must be a list")
        self.el_list = el_list
        self.current = len(self.el_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            self.current -= 1
            return self.el_list[self.current]
        else:
            raise StopIteration

    def __len__(self):
        return len(self.el_list)

el_list = ['aaa', 1, 2, "dfdfdf", (4, 15, 6), "17"]
for el in ReversedListElements(el_list):
    print(el)

# ReversedListElements(None)


#     Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbersToNIncludingIt:
    def __init__(self, n):
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
        self.n = n
        self.__current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current > self.n:
            raise StopIteration
        result = self.__current
        self.__current += 2
        return result

n = 8
# n = -5
for number in EvenNumbersToNIncludingIt(n):
    print(number)