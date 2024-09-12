from websocket import frame_buffer


def celsius_fahrenheit(temperatura):
    return ((temperatura * 9) / 5) + 32

def main():
    print("== Conversor de Temperatura ==")
    print("   Celsius x Fahrenheit ")
    temperatura = float(input("Insira a temperatura em Celsius: "))
    
    print(f"{temperatura}°C corresponde a {celsius_fahrenheit(temperatura)}°F")

if __name__ == "__main__":
    main()
    