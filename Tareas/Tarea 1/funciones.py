import matplotlib.pyplot as plt
import numpy as np


def histograma(img):
    """Cuenta de píxeles por nivel de intensidad, 0 a 255."""
    return np.bincount(img.ravel(), minlength=256)

def triptico(original, transformada, lut, titulo=""):
    """Imagen resultante, curva de transformación y ambos histogramas.

    La curva se dibuja a partir de la LUT: es literalmente la tabla que se aplicó,
    no una reconstrucción teórica de ella.
    """
    fig, ax = plt.subplots(1, 3, figsize=(12.5, 3.8))
    fig.subplots_adjust(wspace=0.55)

    ax[0].imshow(transformada, cmap="gray", vmin=0, vmax=255)
    ax[0].set_title(titulo or "resultado")
    ax[0].axis("off")

    ax[1].plot([0, 255], [0, 255], "--", lw=0.8, color="gray")   # identidad, de referencia
    ax[1].plot(np.arange(256), lut, lw=1.6)
    ax[1].set(xlim=(0, 255), ylim=(0, 255), xlabel="r (entrada)", ylabel="s = T(r)",
              title="función de transformación", aspect="equal")

    ax[2].plot(histograma(original), lw=0.9, alpha=0.55, label="original")
    ax[2].plot(histograma(transformada), lw=0.9, label="transformada")
    ax[2].set(xlim=(0, 255), xlabel="nivel", title="histograma")
    ax[2].legend(fontsize=7)
    plt.show()

def mostrar(imagenes, titulos, filas=1, figsize=None):
    n = len(imagenes)
    cols = int(np.ceil(n / filas))
    fig, axes = plt.subplots(filas, cols, figsize=figsize or (2.9 * cols, 3.1 * filas))
    for ax, im, t in zip(np.atleast_1d(axes).ravel(), imagenes, titulos):
        ax.imshow(im, cmap=None if im.ndim == 3 else "gray",
                  **({} if im.ndim == 3 else dict(vmin=0, vmax=255)))
        ax.set_title(t)
        ax.axis("off")
    for ax in np.atleast_1d(axes).ravel()[n:]:
        ax.axis("off")
    plt.show()

def niveles_usados(img):
    """Cuántos de los 256 niveles posibles aparecen efectivamente en la imagen."""
    return len(np.unique(img))

def entropia(img):
    """Entropía de primer orden en bits/píxel: cuánta información porta el histograma."""
    p = histograma(img).astype(np.float64)
    p = p[p > 0] / img.size
    return -(p * np.log2(p)).sum()

def mostrar_histogramas(histogramas, titulos, filas=1, figsize=None):
    n = len(histogramas)
    cols = int(np.ceil(n / filas))
    fig, axes = plt.subplots(filas, cols, figsize=figsize or (2.9 * cols, 3.1 * filas))
    for ax, h, t in zip(np.atleast_1d(axes).ravel(), histogramas, titulos):
        ax.plot(h, lw=0.9)
        ax.set(xlim=(0, 255), xlabel="nivel", title=t)
    for ax in np.atleast_1d(axes).ravel()[n:]:
        ax.axis("off")
    plt.show()
