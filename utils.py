### Helper funcs for working with lists
import numpy as np


def convert_to_rectangle(r):
    cardinality = r[1]
    side = r[0][0]
    lists = []
    for i in range(1,cardinality+1):
        r = []
        for j in range(side):
            l = [1]*side
            r.append(l)
        lists.append(tuple((f'R{side}_{i}',r)))
    return lists


def create_l(side1, side2):
    l = [[1]*side1 if i==0 else [0]*side1 for i in range(side2)]
    l = np.asarray(l)
    l[:,0] = [1]*side2
    return l.tolist()

def convert_to_Ltetra(r):
    cardinality = r[1]
    side1 = r[0][0]
    side2 = r[0][1]
    lists = []
    for i in range(1, cardinality+1):
        r = create_l(side1, side2)
        lists.append(tuple(((f'L{side1}{side2}_{i}',r))))
    return lists



def check_area(grid_area, rs, ls):

    r_area = sum([(el[0][0] ** 2) * el[0][1] for el in rs])
    l_area = sum([(sum(el[0][i] for i in range(len(el[0]))) - 1) * el[1] for el in ls])

    return True if grid_area > r_area + l_area else False


def check_lengths(m1, m2, rs, ls):

    temp = rs + ls
    max_tuple = max(temp, key=lambda item: max(item[0]))
    m = max(max_tuple[0])

    return True if m > max(m1,m2) else False