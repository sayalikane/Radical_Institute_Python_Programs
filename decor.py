#def decor(func):
    #def wrap():
#    print("$$$$$$")
#    func()
#    print("$$$$$$")
    #return wrap
#def sayhello():
#    print("Hello")
#newfunc=decor(sayhello)

#newfunc()

def decor(func):
    def wrap(a,b):
        if b==0:
            print("Division by 0 not possible")
            return
        return func(a,b)
    return wrap
@decor
def div(a,b):
    x=a/b
    print(x)


div(2,0)
#decor(div)(10,0)
#newfunc()