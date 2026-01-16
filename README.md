# Proyecto 1: Demostración de Regresión 

## Descripción
Este proyecto presenta una demostración visual animada desarrollada con la librería **Manim** (Community Edition).

El objetivo es ilustrar de manera interactiva los conceptos de **Regresión Lineal** y **Regresión No Lineal**, demostrando cómo se ajustan los modelos matemáticos a diferentes distribuciones de datos y visualizando errores comunes en el subajuste.

## Autores - Grupo 3
Integrantes del equipo encargados del desarrollo:

* **Angel Oriundo, Carlos Enrique**
* **Terrazo Santiago, Jean Luka**
* **Villanueva Lara, Carlos Armando**

## Requisitos del Sistema
Para ejecutar este proyecto, es necesario tener instalado el siguiente software:

1.  **Python 3.7+**
2.  **FFmpeg** (Motor de procesamiento de video)
3.  **Manim Community Edition** (Librería de Python)

### Instrucciones de Instalación

#### 1. Instalar FFmpeg
Manim requiere FFmpeg para generar el archivo de video.

* **Windows (Recomendado):**
    Abre la terminal de python y ejecuta el siguiente comando automático:
    ```powershell
    winget install ffmpeg
    ```
    *(Reinicia tu editor de código después de instalar para aplicar los cambios).*

* **MacOS:**
    ```bash
    brew install ffmpeg
    ```

* **Linux:**
    ```bash
    sudo apt install ffmpeg
    ```

#### 2. Instalar Librerías de Python
Ejecuta el siguiente comando para instalar Manim y sus dependencias (NumPy, SciPy, etc.):

```bash
pip install manim
