a=complex(input("Enter a complex number: "))
ty=input("Do you want to get the answer in integer(i) or decimal(d): ")
if ty=="i" or "integer" or "Integer":
    print(f'''
    Real part= {int(a.real)}
    Imaginary part= {int(a.imag)}
    ''')
elif ty== "d" or "decimal" or "Decimal":
    print(f'''
    Real part= {a.real}
    Imaginary part= {a.imag}
    ''')
else:
    print("Please enter a valid input: ")
