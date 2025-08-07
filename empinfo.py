import emp
import salary
k=emp.getdetails()
ta=int(input("enter ta percentage"))
da=float(input("enter da %"))
hra=float(input("enter hra %"))
month=float(input("enter salary"))
s=salary.sal(ta,da,hra,month)
print("emp id is",k[0])
print("emp name is",k[1])
print("emp mail is",k[2])
print("emp address is",k[3])
print("salary is",s)
