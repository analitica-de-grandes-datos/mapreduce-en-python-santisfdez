#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        prueba = line.split()
        for word in prueba[1].split(','):
            sys.stdout.write("{}\t{}\n".format(word, prueba[0]))
