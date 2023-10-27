X = 2
def Moo():
    global X
    X = 5
    return X
X = Moo() + X
print(X)