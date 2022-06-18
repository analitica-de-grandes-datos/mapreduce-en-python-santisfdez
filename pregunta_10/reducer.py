#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    total = 0

    for line in sys.stdin:
        key, val = line.split()
        val = val.strip()

        if key == curkey:
            cadena = cadena + ',' + val
            lista = cadena.split(',')
            lista = sorted(int(i) for i in lista)
            lista = ','.join(str(i) for i in lista)
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, lista))

            curkey = key
            cadena = val

    sys.stdout.write("{}\t{}\n".format(curkey, lista))
