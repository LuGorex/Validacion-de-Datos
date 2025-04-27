# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 16:39:16 2025

@author: luis-
"""

from jsonschema import validate, ValidationError

# Esquema JSON para validar todos los datos del usuario
esquema_completo = {
    "type": "object",
    "properties": {
        "nombre": {"type": "string"},
        "edad": {"type": "integer", "minimum": 18},
        "correo": {"type": "string", "format": "email"}
    },
    "required": ["nombre", "edad", "correo"],
    "additionalProperties": False
}

# Esquema JSON para validar solo correos electrónicos con expresiones regulares
esquema_correo = {
    "type": "object",
    "properties": {
        "correo": {
            "type": "string",
            "pattern": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        }
    },
    "required": ["correo"],
    "additionalProperties": False
}

# Solicitar datos completos al usuario
print("Por favor ingresa los siguientes datos:")
nombre = input("Nombre: ")
edad = input("Edad: ")
correo = input("Correo electrónico: ")

# Convertir la edad a un número entero
try:
    edad = int(edad)
except ValueError:
    print("La edad debe ser un número entero.")
    exit()

# Crear un diccionario con los datos ingresados
datos_completos = {
    "nombre": nombre,
    "edad": edad,
    "correo": correo
}

# Validar todos los datos del usuario
try:
    validate(instance=datos_completos, schema=esquema_completo)
    print("Los datos completos son válidos.")
except ValidationError as e:
    print("Los datos completos no son válidos.")
    print("Error:", e.message)

# Validar solo el correo electrónico con esquema más estricto
datos_correo = {"correo": correo}

try:
    validate(instance=datos_correo, schema=esquema_correo)
    print("El correo electrónico es válido.")
except ValidationError as e:
    print("El correo electrónico no es válido.")
    print("Error:", e.message)
    