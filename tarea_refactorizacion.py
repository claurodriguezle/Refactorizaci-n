def mostrar_menu():
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')

def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point <= 0 or point > 5:
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def mostrar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            content = read_file.read()
            if content:  
                print(content)
            else:
                print("No hay resultados hasta ahora.")
    except FileNotFoundError:
        print("El archivo data.txt no existe. Asegúrate de que se haya creado correctamente.")

def finalizar_proceso():
    print('Finalizando')
    exit()

def main():
    while True:
        mostrar_menu()
        print("Esperando entrada: ")
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                finalizar_proceso()
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

if __name__ == "__main__":
    main()
