from polyo import *
from utils import *

def main(m1, m2, rs, ls):

    #check if there are any polyominos that can't be fit to grid
    if not check_lengths(m1, m2, rs, ls):
        return False
    # grid area must be greater than the area of polyominos
    if not check_area(m1*m2, rs, ls):
        return False

    # some conversions
    r = [convert_to_rectangle(r) for r in rs]
    r = [r[i][j] for i in range(len(r)) for j in range(len(r[i]))]
    l = [convert_to_Ltetra(l) for l in ls]
    l = [l[i][j] for i in range(len(l)) for j in range(len(l[i]))]
    grid = [["." for _ in range(m1)] for _ in range(m2)]

    pentas = [el[1] for el in r] + [el[1] for el in l]
    penta_letters = [el[0] for el in r] + [el[0] for el in l]

    dictionarySetup(pentas, penta_letters, m1, m2)

    impossibles = buildPentaList(len(penta_letters), [], penta_letters, grid)

    if impossibles:
        return False     #does not exist

    else:
        return True      #tiling exists

if __name__ == '__main__':
    # input params
    m1, m2 = 3, 5
    rs = [((2, 2), 1)]
    ls = [((3, 2), 1), ((2, 2), 2)]

    main(m1, m2, rs, ls)
