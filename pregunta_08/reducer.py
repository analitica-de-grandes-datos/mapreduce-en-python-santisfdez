#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None

    sum = 0
    avg = 0
    cont = 0

    for line in sys.stdin:

        key, val, val2 = line.split('\t')
        val = float(val)
        val2 = float(val2)

        if key == curkey:

            sum += val
            cont += val2
            avg = sum/cont
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum, avg))

            curkey = key
            sum = val
            cont = val2
            avg = sum/cont

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum, avg))
