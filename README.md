
### Validación de Datos en Python usando JSON Schema
Este proyecto demuestra cómo validar datos en Python utilizando esquemas JSON. Es ideal para garantizar la calidad y estructura correcta de la información ingresada por los usuarios.

#### **Características**
- **Validación Completa:** Verifica que los datos como nombre, edad y correo cumplan con reglas específicas definidas en un esquema JSON.
- **Validación de Correos Electrónicos:** Implementa expresiones regulares para garantizar que los correos tengan una estructura estrictamente válida.
- **Interacción:** Permite la entrada dinámica de datos por parte del usuario, haciendo el programa fácil de usar.
- **Biblioteca Utilizada:** `jsonschema`, que simplifica la validación contra esquemas JSON.

#### **Requisitos**
- Python 3.x
- Biblioteca `jsonschema` instalada (puedes hacerlo con `pip install jsonschema`).

#### **Uso**
1. Ejecuta el script en tu terminal.
2. Ingresa los datos solicitados (nombre, edad y correo electrónico).
3. El programa validará los datos y te informará si son válidos o no.


#### **Un ejemplo**
Aqui se ingreso por error una edad de 10 cuando debe de ser mayor a 18 y ademas se ingreso una coma en vez de un punto en el correo

![image](https://github.com/user-attachments/assets/2eed22bc-c4ef-4aea-82a5-21c549189abe)

Aqui esta el ejemplo correcto

![image](https://github.com/user-attachments/assets/60e4646c-0e7d-4b09-9e49-11c3d2000a04)


