# ParqueaderoProject
Evaluacion de Producto Primer Momento Nuevas Tecnologias

## 1. Introducción

Este proyecto corresponde al primer momento evaluativo de la materia Nuevas Tecnologías. Se desarrolló un sistema en Python que permite simular la gestión de un parqueadero con funciones básicas como el registro de ingreso y salida de vehículos, el cálculo del tiempo estacionado y el cobro de la tarifa respectiva.

## 2. Objetivo

El objetivo principal es aplicar la lógica de programación y el uso de estructuras de datos en Python para resolver un problema cotidiano, en este caso, la administración de un parqueadero pequeño.

## 3. Características del sistema

Capacidad máxima del parqueadero: 10 vehículos.

Tipos de vehículos admitidos: Carro y Moto.

Tarifas por hora (totalmente modificables):

 - Carro: $3000

 - Moto: $1600

Registro de información de cada vehículo (placa, tipo, hora de entrada y salida).

Validación de errores, como: parqueadero lleno, vehículo ya registrado o tipo de vehículo inválido.

## 4. Funcionalidades principales

Registrar ingreso: Solicita placa, tipo de vehículo y hora de entrada.

Registrar salida: Calcula las horas estacionadas y el total a pagar según la tarifa.

Mostrar vehículos: Lista todos los vehículos actualmente estacionados.

Salir: Termina la ejecución del programa.

## 5. Funcionamiento del cálculo de tarifa

Se convierte la hora de entrada y salida a minutos.

Se calcula la diferencia entre ambas horas (considerando si pasa de medianoche).

Se obtiene el número de horas a cobrar (redondeando hacia arriba).

Se multiplica por la tarifa correspondiente al tipo de vehículo.
