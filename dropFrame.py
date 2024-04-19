from shutil import copyfile
from jdt import Jdt
import os

F_MAX = 5480
RATIO = 10

TEMPLATE = 'out%d.png'
PY_OUT = './pyOut/'

def main():
    print('F_MAX =', F_MAX)
    print('RATIO =', RATIO)
    input('enter...')

    print('clearing output dir...')
    os.system(f'rm {PY_OUT}*.png')
    k = 0
    with Jdt(F_MAX) as j:
        for i in range(1, F_MAX, RATIO):
            j.update(i)
            k += 1
            copyfile('./output/' + TEMPLATE % i, PY_OUT + TEMPLATE % k)
    input('enter...')

main()
