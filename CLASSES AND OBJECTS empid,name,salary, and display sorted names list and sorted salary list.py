class employee:
     def __init__(self):
          num=int(input("How many students you entered:"))
          self.list1=[[] for x in range(num)]
          for x in range(num):
                empid=int(input("Enter emp id:"))
                self.list1[x].append(empid)
                
                name=input("Enter name:")
                self.list1[x].append(name)

                salary=int(input("Enter salary:"))
                self.list1[x].append(salary)
                
          
     def sorted_list(self):
                self.list1.sort(key=lambda x:x[1])
                return self.list1
     def sort_salary(self):
                self.list1.sort(key=lambda x:x[2],reverse=True)
                return self.list1
          
          
                
          

e1=employee()
print("sorted names list:",e1.sorted_list())

print("sorted salary list:",e1.sort_salary())






