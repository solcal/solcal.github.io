a=complex(input("Enter the complex number/expression: "))
abc = input("Do you want to print the answer in integer or decimal (i/d)")
if abc == "d":
    print(f'''
    Real part= {a.real}
    Imaginary part= {a.imag}
    ''')
elif abc == "i":
    print(f'''
    Real part= {int(a.real)}
    Imaginary part= {int(a.imag)}
    ''')
else:
    print("Please input d for getting decimal answer or f for getting a integer answer")
