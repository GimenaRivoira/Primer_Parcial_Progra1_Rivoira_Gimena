def validaciones(minimo, maximo):
    numero_usuario = input(f"Ingrese un numero del {minimo} al {maximo} ")
    
    if int(numero_usuario) < minimo or int(numero_usuario) > maximo:
        return validaciones(minimo, maximo)
    else: 
        return int(numero_usuario)