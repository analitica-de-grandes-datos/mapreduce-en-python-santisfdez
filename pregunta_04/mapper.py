#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        word = line.split()
        sys.stdout.write("{},1\n".format(word[0]))
