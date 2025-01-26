from scipy.optimize import minimize_scalar

# Задание 1. Функция для перемножения матриц с помощью списков и циклов.
# Вернуть нужно матрицу в формате списка.
def matrix_multiplication(matrix_a, matrix_b):
    """
    Перемножение двух матриц, представленных в виде списков.
    :param matrix_a: Первая матрица
    :param matrix_b: Вторая матрица
    :return: Результирующая матрица
    """
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError

    rows_res_len = len(matrix_a)
    cols_res_len = len(matrix_b[0])
    res = []

    for i in range(rows_res_len):
        res.append([])
        for j in range(cols_res_len):
            sm = 0
            for k in range(len(matrix_b)):
                sm += (matrix_a[i][k] * matrix_b[k][j])
            res[i].append(sm)
    return res

# Задание 2. Функция для нахождения точек экстремума двух квадратичных функций и проверки наличия общих решений.
# Вернуть нужно координаты решений списком, если они есть, либо None, если их бесконечно много.
def functions(a_1, a_2):
    """
    Нахождение точек экстремума двух квадратичных функций и их общих решений.
    :param a_1: Коэффициенты первой функции в формате "a b c"
    :param a_2: Коэффициенты второй функции в формате "a b c"
    :return: Координаты общих решений или None, если их бесконечно много
    """

    def f(x, a, b, c):
        return a * x ** 2 + b * x + c

    def find_extremum(a, b, c):
        def g(x):
            return a * x ** 2 + b * x + c

        result = minimize_scalar(g)
        return result.x, f(result.x, a, b, c)

    a1, b1, c1 = map(int, a_1.split())
    a2, b2, c2 = map(int, a_2.split())

    extremum1 = find_extremum(a1, b1, c1)
    extremum2 = find_extremum(a2, b2, c2)

    print(extremum1, extremum2)

    a = a1 - a2
    b = b1 - b2
    c = c1 - c2

    if a == 0 and b == 0 and c == 0:
        return None

    if a != 0:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return []
        else:
            x1 = (-b + d ** 0.5) / 2 * a
            x2 = (-b - d ** 0.5) / 2 * a
            print(x1, x2, a, b, c)
            if x1 == x2:
                return [x1, a1 * x1 ** 2 + b1 * x1 + c1]
            else:
                return [(x1, a1 * x1 ** 2 + b1 * x1 + c1), (x2, a1 * x2 ** 2 + b1 * x2 + c1)]
    elif b != 0:
        x = -c / b
        return [(x, f(x, a, b, c))]
    else:
        return []

# Задание 3. Функции для расчета коэффициента асимметрии и коэффициента эксцесса.
# Оба значения должны быть округлены до двух знаков после запятой.

def skew(x):
    """
    Расчет коэффициента асимметрии.
    :param x: Список чисел
    :return: Коэффициент асимметрии, округленный до 2 знаков
    """
    x_i = sum(x) / len(x)
    sigma = (sum([(num - x_i) ** 2 for num in x]) / len(x)) ** 0.5
    m3 = (sum([(num - x_i) ** 3 for num in x]) / len(x))
    a3 = m3 / sigma ** 3
    return round(a3, 2)

def kurtosis(x):
    """
    Расчет коэффициента эксцесса.
    :param x: Список чисел
    :return: Коэффициент эксцесса, округленный до 2 знаков
    """
    x_i = sum(x) / len(x)
    sigma = (sum([(num - x_i) ** 2 for num in x]) / len(x)) ** 0.5
    m4 = (sum([(num - x_i) ** 4 for num in x]) / len(x))
    e4 = m4 / sigma ** 4 - 3
    return round(e4, 2)
