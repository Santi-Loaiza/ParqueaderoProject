# Informacion fija del parqueadero
CAPACIDAD_TOTAL = 10
TARIFA_POR_HORA = {'Carro': 3000, 'Moto': 1600}

# Para guardar los vehículos
vehiculos_estacionados = []


# Funciones pa calcular
def convertir_minutos(hora_str):
    horas, minutos = hora_str.split(':')
    return int(horas) * 60 + int(minutos)


def tiempo_estacionado(hora_entrada_str, hora_salida_str):
    entrada_min = convertir_minutos(hora_entrada_str)
    salida_min = convertir_minutos(hora_salida_str)
    if salida_min < entrada_min:  # pasó medianoche
        salida_min += 24 * 60
    total_min = salida_min - entrada_min
    horas = total_min // 60
    if total_min % 60 != 0:
        horas += 1
    return horas


def calcular_tarifa(tipo_vehiculo, horas):
    return TARIFA_POR_HORA[tipo_vehiculo] * horas


# Funciones de registro
def registrar_ingreso():
    if len(vehiculos_estacionados) >= CAPACIDAD_TOTAL:
        print("El PARQUEADERO ESTA LLENO".center(60, ' '))
        return

    placa = input("Ingrese la placa: ").upper()
    for v in vehiculos_estacionados:
        if v['datos'][0] == placa:
            print("⚠️ Este vehículo ya está registrado en el parqueadero.".center(60, ' '))
            return

    tipo = input("Ingrese el tipo de vehículo (Carro/Moto): ").capitalize()
    if tipo not in ["Carro", "Moto"]:
        print("⚠️ Tipo de vehículo inválido.".center(60, ' '))
        return
    if tipo == "Carro" and not placa[-1].isdigit():
        print("OJO. La placa de un carro no termina en una letra.".center(60, ' '))
        return
    if tipo == "Moto" and not placa[-1].isalpha():
        print("OJO. La placa de una moto no termina en un número.".center(60, ' '))
        return

    hora_entrada = input("Ingrese la hora de entrada (HH:MM): ")

    vehiculo = {
        'datos': (placa, tipo),
        'hora_entrada': hora_entrada,
        'hora_salida': None
    }
    vehiculos_estacionados.append(vehiculo)
    print(f"✅ Vehículo {placa} registrado con éxito.".center(60, ' '))


def registrar_salida():
    placa = input("Ingrese la placa: ").upper()

    for v in vehiculos_estacionados:
        if v['datos'][0] == placa:
            hora_salida = input("Ingrese la hora de salida (HH:MM): ")
            v['hora_salida'] = hora_salida

            horas = tiempo_estacionado(v['hora_entrada'], v['hora_salida'])
            tarifa = calcular_tarifa(v['datos'][1], horas)

            print(f"Tiempo estacionado: {horas} horas")
            print(f"Total a pagar: ${tarifa}")
            vehiculos_estacionados.remove(v)
            print("🚗 Vehículo retirado del parqueadero.".center(60, ' '))
            return

    print("⚠️ Este vehículo no está registrado en el parqueadero.".center(60, ' '))


def mostrar_vehiculos():
    if not vehiculos_estacionados:
        print("No hay vehículos estacionados.")
        return
    print("\nVehículos en el parqueadero".center(60,"-"))
    for v in vehiculos_estacionados:
        placa, tipo = v['datos']
        print(f"Placa: {placa} | Tipo: {tipo} | Entrada: {v['hora_entrada']} | Salida: {v['hora_salida']}")
    print("".center(60, '-'))


# Menu para el parqueadero
def programaParqueadero():
    while True:
        print('PARQUEADERO'.center(60,' '))
        print("1. Registrar ingreso".center(60,' '))
        print("2. Registrar salida".center(60,' '))
        print("3. Mostrar vehículos".center(60,' '))
        print("4. Salir".center(60, ' '))

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_ingreso()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            mostrar_vehiculos()
        elif opcion == "4":
            print("👋 Saliendo del parqueadero. Chaito".center(60, ' '))
            break
        else:
            print("⚠️ Opción inválida.".center(60, ' '))


# Ejecutar el programa
programaParqueadero()
