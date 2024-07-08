def es_as_privado(as_numero):
    as_privados = [
        (64512, 65534),
        (4200000000, 4294967294)
    ]
    
    for inicio, fin in as_privados:
        if inicio <= as_numero <= fin:
            return True
    return False

def main():
    try:
        as_numero = int(input("Ingrese el número de AS de BGP: "))
        
        if es_as_privado(as_numero):
            print(f"El número de AS {as_numero} es un AS privado.")
        else:
            print(f"El número de AS {as_numero} es un AS público.")
    
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
