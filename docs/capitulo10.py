import matplotlib.pyplot as plt
import numpy as np

def graficar_intervalo_confianza(lower_bound, upper_bound, title='Intervalo de Confianza'):
    # Creando datos para la curva de densidad (aproximación de una distribución normal)
    x = np.linspace(lower_bound - 1, upper_bound + 1, 1000)
    mean = (lower_bound + upper_bound) / 2
    std_dev = (upper_bound - lower_bound) / 4  # Estimación aproximada para la desviación estándar
    y = np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

    # Creando la figura y el eje
    fig, ax = plt.subplots()

    # Dibujando la línea numérica
    ax.plot([lower_bound - 1, upper_bound + 1], [0, 0], color='black', lw=2)

    # Dibujando la curva de densidad
    ax.plot(x, y, color='green')

    # Sombreado de las áreas a los extremos del intervalo de confianza
    ax.fill_between(x, y, where=(x < lower_bound) | (x > upper_bound), color='blue', alpha=0.3)

    # Configuración del gráfico
    ax.set_xlim(lower_bound - 1, upper_bound + 1)
    ax.set_ylim(-0.1, 1.1)
    ax.set_yticks([])
    ax.set_xticks([lower_bound, upper_bound])
    ax.set_xticklabels([f'{lower_bound:.2f}', f'{upper_bound:.2f}'])

    # Añadiendo título
    ax.set_title(title)

    # Mostrando el gráfico
    plt.show()

# Ejemplo de uso de la función para el intervalo de confianza del 90%
graficar_intervalo_confianza(1.021425638867089, 2.978574361132911, 'Intervalo de Confianza del 90%')

# Ejemplo de uso de la función para el intervalo de confianza del 95%
graficar_intervalo_confianza(0.8339567286789442, 3.1660432713210556, 'Intervalo de Confianza del 95%')
