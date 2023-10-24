# SGSSI-LAB-06

## Descripcion
Este programa en Python verifica archivos de texto en un directorio en busca de archivos que cumplan ciertas condiciones de comparación con un archivo de entrada. Las condiciones incluyen la igualdad de contenido al principio y un formato específico en el contenido restante. El programa calcula el resumen SHA-256 de los archivos y muestra los archivos que cumplen las condiciones, ordenados por el número de ceros iniciales en su resumen SHA-256. Si no se encuentran archivos que cumplan las condiciones, el programa informa que no se encontraron coincidencias.
## Descargar
- Puede copiar el archivo '.py' y crear uno nuevo con el nombre que quieras (Te aconsejo que sigas con el mismo de este repositorio para poder seguir los siguientes pasos) con el sufijo '.py'
## Requisitos
- Tener python
## Ejecutar el codigo
Primero abre la terminal.
Puede haber dos maneras de ejecutarlo, en caso de que no te funcione con una, hazlo con la otra:
```bash
  - py .\{Nombre del fichero}.py
  - Ingrese la ruta del archivo de entrada: ./{ubicacion}/{Nombre del fichero}.txt
  - Ingrese la ruta del directorio con archivos de texto: ./{ubicacion}/{Nombre de la carpeta}
```
Ejemplo:
```bash
  - py .\resumenSHA-256-6-1.py
  - Ingrese la ruta del archivo de entrada: ./SGSSI-23.CB.03.txt
  - Ingrese la ruta del directorio con archivos de texto: ./SGSSI-23.S.6.2.CB.03.Candidatos
```
El otro metodo, seria cambiar py por python3.

# SGSSI-LAB-06

# Copyright (c) 2023 Carlos Diez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
