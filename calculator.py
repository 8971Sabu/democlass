class calculator:
    def __init__(subbi,a,b):
        subbi.a=a
        subbi.b=b
    def add(subbi):
        return subbi.a+subbi.b
    def sustract(subbi):
        return subbi.a-subbi.b
    def multiply(subbi):
        return subbi.a*subbi.b
    def divide(subbi):
        return subbi.a/subbi.b
calc=calculator(10,5)
print("Addition",calc.add())
print("sustraction",calc.sustract())
print("multiplication",calc.multiply())
print("division",calc.divide())        