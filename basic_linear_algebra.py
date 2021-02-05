def vector_size_check(*vector_variables):
    return len(set([len(i) for i in vector_variables]))==1


def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables)==True:
        return [sum(i) for i in zip(*vector_variables)]
    else:
        raise ArithmeticError


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    else:
        return [i[0]*2-sum(i) for i in zip(*vector_variables)]


def scalar_vector_product(alpha, vector_variable):
    return [alpha*i for i in vector_variable]


def matrix_size_check(*matrix_variables):
    return len(set(len(i) for i in matrix_variables))==1


def is_matrix_equal(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    else:
        return all([all([len(set(j)) ==1 for j in zip(*i)]) for i in zip(*matrix_variables)])


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[sum(j) for j in zip(*i)] for i in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[j[0]*2- sum(j) for j in zip(*i)] for i in zip(*matrix_variables)]


def matrix_transpose(matrix_variable):
    return [[j for j in i]for i in zip(*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha*j for j in i] for i in matrix_variable]

def is_product_availability_matrix(matrix_a, matrix_b):
    return True and len(matrix_a[0]) == len(matrix_b)


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return [[sum(a*b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
