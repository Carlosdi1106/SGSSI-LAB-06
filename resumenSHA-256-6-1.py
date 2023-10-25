import os
import hashlib
import re

def calcular_sha256(file_path):
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
            sha256_hash = hashlib.sha256()
            sha256_hash.update(file_content)
            return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    except Exception as e:
        return str(e)

def comprobar_archivos(archivo1, archivo2):
    try:
        with open(archivo1, "r") as file1, open(archivo2, "r") as file2:
            contenido1 = file1.read()
            contenido2 = file2.read()

            lineas1 = contenido1.split('\n')
            lineas2 = contenido2.split('\n')
            if len(lineas2) == len(lineas1):

                if contenido2.startswith(contenido1):
                    sha256_summary = calcular_sha256(archivo2)

                    if sha256_summary.startswith('00'):
                        remaining_content = contenido2[len(contenido1):]
                        expected_format_1 = r"^[0-9a-f]{8}\t[0-9a-f]{2}\t100$"
                        expected_format_2 = r"^[0-9a-f]{8}[ ]+[0-9a-f]{2}[ ]+100$"
                        if re.match(expected_format_1, remaining_content):
                            prefix_zeros = len(re.match(r"^0+", sha256_summary).group())
                            return True, prefix_zeros
                        if re.match(expected_format_2, remaining_content):
                            prefix_zeros = len(re.match(r"^0+", sha256_summary).group())
                            return True, prefix_zeros

        return False, 0
    except Exception as e:
        return False, 0

def main():
    archivo1 = input("Ingrese la ruta del archivo de entrada: ")
    directorio = input("Ingrese la ruta del directorio con archivos de texto: ")

    if not os.path.isfile(archivo1):
        print(f"El archivo de entrada {archivo1} no existe.")
        return

    if not os.path.isdir(directorio):
        print(f"El directorio {directorio} no existe.")
        return

    archivos_cumplen_condiciones = []

    for root, dirs, files in os.walk(directorio):
        for file in files:
            archivo2 = os.path.join(root, file)
            cumple_condiciones, prefix_zeros = comprobar_archivos(archivo1, archivo2)
            if cumple_condiciones:
                archivos_cumplen_condiciones.append((archivo2, prefix_zeros))

    if archivos_cumplen_condiciones:
        print("Archivos que cumplen las condiciones:")
        archivos_cumplen_condiciones.sort(key=lambda x: x[1], reverse=True)
        for archivo, prefix_zeros in archivos_cumplen_condiciones:
            print(f"{archivo} - Número de ceros iniciales en el resumen SHA-256: {prefix_zeros}")


        
        # Seleccionar el primer archivo de la lista ordenada
        mejor_archivo = archivos_cumplen_condiciones[0][0]
        mejor_prefix_zeros = archivos_cumplen_condiciones[0][1]
        print(f"Archivo con el mayor número de ceros iniciales ({mejor_prefix_zeros}): {mejor_archivo}")
    else:
        print("No se encontraron archivos que cumplan las condiciones.")

if __name__ == "__main__":
    main()
