
def decoratora(foo):
    def wraper(*args):
        print('Before')
        foo(*args)
        print('After')
    return wraper

def psevdo(decor_text):
    def decoratora(foo):
        def wraper(*args):
            print('Before')
            # print((decor_text))
            foo(decor_text)
            foo(*args)
            print('After')
        return wraper
    return decoratora

@psevdo('Hi')
def hart(text):
    print(text)

hart('Hello World')
