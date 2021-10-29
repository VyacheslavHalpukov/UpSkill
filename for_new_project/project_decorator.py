def decoratora(foo):
    def wraper(*args):
        print('Before')
        foo(*args)
        print('After')
    return wraper

@decoratora
def hart(text):
    print(text)

hart('Hello World')
