import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_cubo(a):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    points = np.array([
        [0, 0, 0],
        [a, 0, 0],
        [a, a, 0],
        [0, a, 0],
        [0, 0, a],
        [a, 0, a],
        [a, a, a],
        [0, a, a]
    ])

    faces = [
        [points[j] for j in [0,1,2,3]],
        [points[j] for j in [4,5,6,7]],
        [points[j] for j in [0,1,5,4]],
        [points[j] for j in [1,2,6,5]],
        [points[j] for j in [2,3,7,6]],
        [points[j] for j in [3,0,4,7]]
    ]

    cube = Poly3DCollection(faces, facecolors='cyan', edgecolors='blue', linewidths=1, alpha=0.5)
    ax.add_collection3d(cube)

    ax.set_box_aspect([1,1,1])
    ax.set_xlim(0, a)
    ax.set_ylim(0, a)
    ax.set_zlim(0, a)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Cubo")

    ax.grid(True)
    ax.set_facecolor('white')

    # Para asegurarnos que Streamlit lo renderice bien
    plt.tight_layout()

    return fig

# --- Streamlit App ---

st.title("📐 Calculadora de Volumen de Figuras 3D")

a = st.number_input("Ingrese la arista del cubo:", min_value=0.1, value=1.0, step=0.1)

if st.button("Calcular y mostrar cubo"):
    vol = a**3
    st.success(f"Volumen del cubo: {vol:.4f} unidades cúbicas")

    fig = plot_cubo(a)
    st.pyplot(fig)
    plt.close(fig)  # Cerramos la figura para liberar memoria
