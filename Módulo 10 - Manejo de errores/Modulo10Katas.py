"""def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()
"""
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()

def aguaRestante(astronautas, agua_left, dias_left):
    for item in [astronautas, agua_left, dias_left]:
        try:
            item / 10
        except TypeError:
            raise TypeError(f"Los argumentos recibidos no son enteros: '{item}'")
    diaUso = astronautas * 11
    totalUso = diaUso * dias_left
    totalAguaRestante = agua_left - totalUso
    if totalAguaRestante < 0:
        raise RuntimeError(f"No hay agua para {astronautas} astronautas despues {dias_left} dias")
    return f"Agua restante para {dias_left} dias es: {totalAguaRestante} litros"

print(aguaRestante(5,1000,7))