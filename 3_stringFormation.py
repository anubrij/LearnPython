#string formation
#we can inject variable in string by {}
#to formate the string with variable we need to prefix 'f' before start of string
#example f"name {first_name}
first_name = "Anubrij"
last_name = "Chandra"
mobile = "+919891253473"
address = "c-1020, gaur city, G. Noida"
print(f"My name is {first_name} {last_name}")
print(f"Mobile no is {mobile}")
print(f"Address : {address}")

#some more string formation
a = "1"
b = "2"
c = "3"
d = "4"
print(a + b + c + d , end=' abc ')
print(a + b + c + d)

#paragraph print with triple quotes
print("""once upon a times .
         a fox is jump over as
         quick lazy dog.
      """)
