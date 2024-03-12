#python comments-this is a single
"""
this is a muliple line comment
"""

#variables
student_name = "Jonathan" #datatype is string
student_age =20 #datatype is integer
student_fee=100.00 #datatype is float
is_male=True #datatype is boolean

#outputting the data in variables
print(student_name)
print(student_age)
print(student_fee)
print(is_male)


student_name="Oscar"
student_name="Kimani"
print(student_name)


STUDENT_NAME="Jonathan"
student_name="Daniel"
print(STUDENT_NAME)

#variable meaning in python
book_price=20.0 #valid variable name
_book_price=20.0 #valid variable name
#*book_price=10.0
#123_book_price=10.0
book_price_123=10.0

x=y=z=10 #assigning one value to multiple variables
x,y,z=20,30,40 #assigning different values to different variables

age=17
residency="nairobian"

if residency=="nairobian" or age>=18:
    print("you can be governor")
else:
    print("you can not be governor")