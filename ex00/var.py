def type_var(var):
    print(var, end='')
    print(" est de type ", end='')
    print(type(var))

def my_var():
    type_var(42)
    type_var("42")
    type_var("quarante-deux")
    type_var(42.0)
    type_var(True)
    type_var([42])
    type_var({42: 42})
    type_var((42,))
    type_var(set())

if __name__ == '__main__':
    my_var()