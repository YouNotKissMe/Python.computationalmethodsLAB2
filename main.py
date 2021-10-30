''' Мой вариант 8 система из 4 уравнений -83x1+27x2-13x3-11x4=142
                                          5x1-68x2+13x3+24x4=26
                                          9x1+54x2+127x3+36x4=23
                                          13x1+27x2+34x3+156x4=49
1. Решить систему линейных алгебраических уравнений, используя:

# 1.2. метод Гаусса с выбором ведущего элемента по строке;

# 1.3. метод Гаусса с выбором ведущего элемента по столбцу;

# 1.4. метод Гаусса с выбором ведущего элемента во всей матрице А;

1.5. LU-алгоритм.

2. Оценить погрешность полученных решений по правой части.

3. Вычислить определитель матрицы А, используя указанные выше методы.

4. Построить обратную матрицу А, используя метод Гаусса. '''


# -----------------------------------------------Метод Гаусса ---------------------------------------------------------

class Gauss:
    def __init__(self):
        self.__matrix = [[-83, 27, -13, -11, 142],
                         [5, -68, 13, 24, 26],
                         [9, 54, 127, 36, 23],
                         [13, 27, 34, 156, 49]]
        self.__n = 0
        self.__result = []

    def metodGauss(self):
        if self.__n == len(self.__matrix):
            print(self.__matrix)
            x4 = self.__matrix[3][4]
            x3 = self.__matrix[2][4] - \
                 self.__matrix[2][3] * x4
            x2 = self.__matrix[1][4] - \
                 self.__matrix[2][3] * x4 \
                 - self.__matrix[1][2] * x3
            x1 = self.__matrix[0][4] \
                 - self.__matrix[2][3] \
                 * x4 - self.__matrix[1][2] * x3 \
                 - self.__matrix[0][1] * x3 * x2
            self.__result = [x1, x2, x3, x4]
            print(self.__result)

        else:
            self.__matrix[self.__n] = list(map(lambda x: x / \
                                        self.__matrix[self.__n][self.__n],
                                        self.__matrix[self.__n]))
            for z in range(self.__n + 1,
                           len(self.__matrix)):

                a = list(map(lambda x: x * \
                                       self.__matrix[z][self.__n],
                                       self.__matrix[self.__n]))
                for i in range(len(self.__matrix) + 1):
                    self.__matrix[z][i] = self.__matrix[z][i] - a[i]
            self.__n += 1
            Gauss.metodGauss(self)
    def GaussWithLine(self):
        qq = []
        if self.__matrix[self.__n][self.__n] == max(self.__matrix[self.__n]):
            print(self.__matrix)
        else:
            print('da', self.__n,self.__matrix[self.__n][self.__n], max(self.__matrix[self.__n]))
            for i in range(len(self.__matrix)):
                a = max(self.__matrix[self.__n])
                a = self.__matrix[self.__n].index(a)
                self.__matrix[i][self.__n], self.__matrix[i][a] = \
                     self.__matrix[i][a], self.__matrix[i][self.__n]


    def GaussWithColumn(self):
        # 1.3. метод Гаусса с выбором ведущего элемента по столбцу;
        pass

    def HardGauss(self):
        # 1.4. метод Гаусса с выбором ведущего элемента во всей матрице А;
        pass

    @property
    def matrix(self):
        return self.__matrix


a = Gauss()
a.metodGauss()




