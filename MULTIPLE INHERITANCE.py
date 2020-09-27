class person:
       def __init__(self,n,a):
           self.name=n
           self.age=a



class student(person):
       def __init__(self,n,a,r):
           self.rollno=r
           person.__init__(self,n,a)

class teacher(person):
       def __init__(self,n,a,s,sub):
           self.salary=s
           self.subject=sub
           person.__init__(self,n,a)


class brightstudent(student,teacher):
      def __init__(self,n,a,r,s,sub,p):
          self.points=p
          student.__init__(self,n,a,r)
          teacher.__init__(self,n,a,s,sub)


obj=brightstudent("Aakash",18,201,20000,"physics",8.0)
