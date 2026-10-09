# Procesamiento de Imágenes

En este repositorio se encuentran las tareas y el material de clase del ramo
**Procesamiento de Imágenes**.

## Preparar el entorno en otro computador

Estas instrucciones permiten trabajar con los notebooks del repositorio en
macOS o Windows. El entorno virtual `.venv` no se sube a GitHub, porque los
entornos virtuales dependen del sistema operativo. Por eso, cada computador
debe crear su propio entorno.

### 1. Instalar los programas necesarios

Instala los siguientes programas:

- [Git](https://git-scm.com/downloads)
- [Python 3.12](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)

En VS Code instala también las extensiones **Python**, **Pylance** y
**Jupyter**.

En Windows, durante la instalación de Python marca la opción **Add Python to
PATH**.

### 2. Clonar el repositorio

Abre una terminal y ejecuta:

#### macOS

```bash
cd ~/Documents
git clone https://github.com/NegroBsky/Procesamiento-de-Imagenes-2026-2.git
cd Procesamiento-de-Imagenes-2026-2
code .
```

#### Windows PowerShell

```powershell
cd $HOME\Documents
git clone https://github.com/NegroBsky/Procesamiento-de-Imagenes-2026-2.git
cd Procesamiento-de-Imagenes-2026-2
code .
```

Si el repositorio ya está clonado, no ejecutes nuevamente `git clone`; entra
directamente a la carpeta del proyecto.

### 3. Crear el entorno virtual

Ejecuta estos comandos desde la carpeta raíz del repositorio:

#### macOS

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si Windows bloquea la activación de scripts, ejecuta una sola vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Después, vuelve a ejecutar:

```powershell
.\.venv\Scripts\Activate.ps1
```

La terminal debe mostrar `(.venv)` al comienzo de la línea. Si cierras la
terminal, tendrás que activar nuevamente el entorno la próxima vez.

### 4. Instalar las dependencias

Con el entorno virtual activado, ejecuta:

#### macOS y Windows

```bash
python -m pip install --upgrade pip
python -m pip install numpy matplotlib scipy scikit-image opencv-python pillow
python -m pip install jupyter ipykernel
python -m pip install torch torchvision torchaudio
python -m pip install ultralytics
```

Estas dependencias cubren las librerías utilizadas por los notebooks y por los
códigos de procesamiento de imágenes, PyTorch y YOLO.

### 5. Registrar el kernel de Jupyter

Ejecuta, con el entorno todavía activado:

```bash
python -m ipykernel install --user --name procesamiento-imagenes --display-name "Python (Procesamiento de Imagenes)"
```

En VS Code, abre un archivo `.ipynb`, selecciona **Select Kernel** y elige
**Python (Procesamiento de Imagenes)** o el intérprete ubicado dentro de
`.venv`.

También puedes seleccionar el intérprete desde la paleta de comandos:

1. Presiona `Ctrl + Shift + P` en Windows o `Cmd + Shift + P` en macOS.
2. Ejecuta **Python: Select Interpreter**.
3. Selecciona el Python ubicado en `.venv`.

### 6. Verificar la instalación

Con `.venv` activado, ejecuta:

```bash
python -c "import numpy, matplotlib, scipy, skimage, cv2, PIL, torch; print('Entorno funcionando correctamente')"
```

También puedes ejecutar esta celda en un notebook:

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
from PIL import Image

print("Todo funciona correctamente")
```

## Datasets y archivos grandes

Algunos datasets o modelos grandes no están incluidos en GitHub. Por ejemplo,
la carpeta `CrackForest-dataset` está excluida del repositorio y debe
descargarse o copiarse manualmente en la ubicación esperada por cada tarea.

Los modelos y datasets deben conservar la estructura de carpetas utilizada por
los notebooks. No se deben utilizar rutas absolutas específicas de un
computador, como:

```python
"/Users/tu_usuario/..."
```

En su lugar, usa rutas relativas o `pathlib`:

```python
from pathlib import Path

ruta_imagen = Path("Clases") / "Clase 05" / "imagenes" / "forest.JPG"
```

De esta manera, el mismo notebook puede ejecutarse en macOS y Windows.

## Flujo de trabajo con Git

Antes de comenzar a trabajar en Windows o macOS, actualiza el repositorio:

```bash
git pull
```

Después de realizar cambios en notebooks o archivos de código:

```bash
git status
git add .
git commit -m "Actualiza cuaderno de procesamiento de imagenes"
git push
```

En el otro computador, ejecuta nuevamente `git pull` para descargar esos
cambios.

No subas `.venv` al repositorio. Esta carpeta ya está incluida en
[`.gitignore`](.gitignore).
