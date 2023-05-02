
class A:
    a=36
    me=2.8
    def aMethod(self):
        print("A class")
    def sadiqa(self):
        print("method of a class")
class B(A):
    b=7.98
    me=7456
    def bmethod(self):
        print("class B ", self.me + super().me, A.me)
    def demo(self):
        print("method of B class")
        super().sadiqa()
class C(B):
    c=41.25
    me=73.25
    def cmethod(self):
        print("class C", self.me + super().me,A.me)
    def demo(self):
        print("method of B class")
        super().demo()
        A.demo(self)
c=C()
c.demo()
c.cmethod()