#Buenas practicas mientras codificas es usar snake_case ejemplo:
my_name= "My name is Deivis"
print(my_name)

sujeto_yo = "I"
sujeto_el = "He"
sujeto_ella = "She"

print(sujeto_yo,sujeto_el,sujeto_ella)

#Variables

greetings = "Hello, Hi"
print(greetings)

greetings = 1
print(greetings)

my_int_to_str_variable = str(greetings)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_name, greetings, sujeto_yo, sujeto_el, sujeto_ella, my_int_to_str_variable,my_bool_variable)
print(type(print((my_name, greetings, sujeto_yo, sujeto_el, sujeto_ella, my_int_to_str_variable,my_bool_variable))))

#Algunas funciones del sistema
print(len(sujeto_yo))

print("Titles:", "Mrs,","Mr,","Miss,","Ms.")

#variables en una sola linea:
name, last_name, age, alias = "Deivis", "Baena", 40, "Daveselv"
print("My name is:", name,", My lastname is:",last_name, ", I am", age,"years old",", My alias is:", alias)

#inputs (solicita datos )
"""
first_name = input("What is your name? ")
Age = input("How old are you? ")
print(first_name,age)

"""

#Python es un lenguaje de tipado Dinamico 
name = 35
Age = "Deivis"

#Forzamos el tipo? es informativo segun el contexto de trabajo

Greetings: str = "Hello"
greetings = 1
print(type(greetings))
print(greetings)