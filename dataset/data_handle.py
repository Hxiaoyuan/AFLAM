import random


def clean_data(path, d, save):
    x = []
    y = []
    with open(path, 'r') as f:
        fs = f.readlines()
        random.shuffle(fs)
        for l in fs:
            l = l.strip()
            ls = l.split(' ')
            if len(ls) == 1:
                continue
            if int(ls[0]) == -1:
                _y = 0
            else:
                _y = int(ls[0])
            _x = [0.] * d
            for ll in ls[1:]:
                lls = ll.split(':')
                _x[int(lls[0])-1] = float(lls[1])
            x.append(_x)
            y.append(_y)
    with open(save+'x.txt', 'w') as f:
        for l in x:
            f.write(' '.join([str(f) for f in l]) + '\n')

    with open(save+'y.txt', 'w') as f:
        for l in y:
            f.write(str(l) + '\n')


if __name__ == '__main__':
    path = './data/a1a.txt'
    save = './data/a1a_clean_'
    d = 123
    clean_data(path, d, save)