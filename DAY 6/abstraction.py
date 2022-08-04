from abc import ABC,abstractmethod
class A(ABC):
     @abstractmethod
     def test1(self):
          pass
     @abstractmethod
     def test2(self):
          pass
class B(A):
     def test1(self):
          print("Hello")
class C(B):
     def test2(self):
         print("Welcome")
obj = C()
obj.test1()
obj.test2()