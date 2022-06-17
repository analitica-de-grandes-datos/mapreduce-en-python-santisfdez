#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    elements = []

    for line in sys.stdin:
        elements.append(line)
else:
    elements = sorted(
                elements,
                key = lambda data: (data,split()[0], int(data.split()[2]))
                )

    for element in elements:
        sys.stdout.write("{}".format(element))
