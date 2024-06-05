def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Escolha a opção:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Fahrenheit para Kelvin")
    print("6. Kelvin para Fahrenheit")
    choice = input("Digite o número da opção desejada: ")

    if choice == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print("A temperatura em Fahrenheit é:", celsius_to_fahrenheit(celsius))
    elif choice == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print("A temperatura em Celsius é:", fahrenheit_to_celsius(fahrenheit))
    elif choice == '3':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print("A temperatura em Kelvin é:", celsius_to_kelvin(celsius))
    elif choice == '4':
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print("A temperatura em Celsius é:", kelvin_to_celsius(kelvin))
    elif choice == '5':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print("A temperatura em Kelvin é:", fahrenheit_to_kelvin(fahrenheit))
    elif choice == '6':
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print("A temperatura em Fahrenheit é:", kelvin_to_fahrenheit(kelvin))
    else:
        print("Escolha inválida. Por favor, escolha uma opção de 1 a 6.")

if __name__ == "__main__":
    main()
