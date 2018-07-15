# Case 1: Method will not be overridden in class B and class C
#  =>"class A method" 
# Case 2: Method will be overriden in class B not class C
# => "class B method"
# Case 3: Method will be overriden in not in class B but in class C
# => "class C mehtod"
# Case 4: Method will be overriden in both the class B and class C
# => "class B method" because B is called first than C
class A:
      def method(self):
          print("class A method")


class B(A):
      def method(self):
          print("class B method")

class C(A):
      def method(self):
          print("class C method")

class D(B, C):
      pass

d = D()
d.method()
