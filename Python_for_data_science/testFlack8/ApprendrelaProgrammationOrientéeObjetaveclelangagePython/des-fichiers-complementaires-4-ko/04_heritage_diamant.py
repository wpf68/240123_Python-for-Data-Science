# Méthode explicite

class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b

class C(A):
    def __init__(self, a, c):
        A.__init__(self, a)
        self.c = c

class D(B, C):
    def __init__(self, a, b, c):
        B.__init__(self, a, b)
        C.__init__(self, a, c)

d = D(1, 2, 3)
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))
print(d.a, d.b, d.c)

# Méthode avec arguments nommés

class A:
    def __init__(self, a_param):
        # A est la classe "de base" et n'a pas d'ancètre à qui passer
        # les arguments, donc pas besoin de **kwargs.
        self.a = a_param

class B(A):
    def __init__(self, b_param, **kwargs):
        # Ici, seul le paramètre 'b_param' est utilisé, et le
        # reste est passé au constructeur de la classe retournée par
        # 'super()'.
        super().__init__(**kwargs)
        self.b = b_param

class C(A):
    def __init__(self, c_param, **kwargs):
        # Ici, seul le paramètre 'c_param' est utilisé, et le reste
        # est passé au constructeur de la classe retournée par
        # 'super()'.
        super().__init__(**kwargs)
        self.c = c_param

class D(B, C):
    def __init__(self, a, b, c):
        # Les arguments sont nommés afin de pouvoir explicitement les
        # utiliser dans les constructeurs des classes-mères.
        super().__init__(a_param = a, b_param = b, c_param = c)

d = D(1, 2, 3)
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))
print(d.a, d.b, d.c)
