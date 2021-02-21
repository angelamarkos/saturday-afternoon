import sys
def echo(string):
    print(string)

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        echo(arg)
