from fibo import fib

if __name__ == "__main__":
    import sys
    print('Ards: ', sys.argv)
    fib(int(sys.argv[1]))