def gen():
    print('hello world')
    yield
    print('bye bye')


def main():
    g = gen()

    print('before generator')

    next(g)

    print('in the middle of generator')

    try:
        next(g)
    except StopIteration:
        pass

    print('after the generator')


if __name__ == '__main__':
    main()
