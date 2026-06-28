# Image to WebP Converter

Convierte automáticamente todas las imágenes de una carpeta al formato **WebP** utilizando Python y la biblioteca **Pillow**.

## Características

- Convierte imágenes a formato WebP.
- Soporta múltiples formatos de entrada:
  - JPG
  - JPEG
  - PNG
  - BMP
  - TIFF
  - GIF
- Conserva la calidad de imagen configurable.
- Crea automáticamente la carpeta de salida.
- Compatible con Windows, Linux y macOS.

## Requisitos

- Python 3.8 o superior
- Pillow

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/usuario/image-to-webp.git
cd image-to-webp
```

Instala las dependencias:

```bash
pip install Pillow
```

O usando un archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Estructura del proyecto

```
image-to-webp/
│
├── images/            # Imágenes originales
├── webp/              # Imágenes convertidas
├── convert.py         # Script principal
├── requirements.txt
└── README.md
```

## Uso

Coloca las imágenes dentro de la carpeta `images`.

Ejecuta el script:

```bash
python main.py
```

Las imágenes convertidas aparecerán en la carpeta:

```
webp/
```

## Configuración

Dentro del script puedes modificar los siguientes parámetros:

```python
quality=85
method=6
```

### Calidad

| Valor | Descripción |
|--------|-------------|
| 100 | Máxima calidad |
| 90 | Excelente calidad |
| 85 | Recomendado |
| 75 | Mayor compresión |
| 50 | Archivos muy pequeños |

### Método de compresión

| Valor | Velocidad | Compresión |
|--------|-----------|------------|
| 0 | Muy rápida | Baja |
| 3 | Media | Buena |
| 6 | Lenta | Máxima |

## Compresión sin pérdida

Si deseas mantener la calidad original:

```python
img.save(
    output_path,
    "WEBP",
    lossless=True,
    method=6
)
```

## Formatos soportados

- JPG
- JPEG
- PNG
- BMP
- TIFF
- GIF

## Ejemplo

Antes:

```
images/
├── foto1.jpg
├── logo.png
└── paisaje.jpeg
```

Después:

```
webp/
├── foto1.webp
├── logo.webp
└── paisaje.webp
```

## Dependencias

- Pillow

Instalación:

```bash
pip install Pillow
```

## Autor

rfalfarop at gmail Desarrollado en Python utilizando Pillow.