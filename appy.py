import streamlit as st
import time

# Preguntas del quiz
questions = [
    {
        "question": "¿Cuál es una característica principal de la licencia MIT?",
        "options": [
            "Permite usar, copiar y modificar sin muchas restricciones",
            "No permite redistribución",
            "Solo se usa para software privado",
            "Tiene muchas cláusulas restrictivas"
        ],
        "answer": 0
    },
    {
        "question": "¿Qué diferencia tiene la licencia BSD respecto a MIT?",
        "options": [
            "Es más restrictiva",
            "No permite uso comercial",
            "Tiene variantes con 2 o 3 cláusulas",
            "Es solo para proyectos gubernamentales"
        ],
        "answer": 2
    },
    {
        "question": "¿Qué buscan las licencias MIT y BSD principalmente?",
        "options": [
            "Control total del autor sobre el software",
            "Flexibilidad y accesibilidad para usar y modificar",
            "Limitar la distribución a solo ciertos países",
            "Garantizar que nadie use el código"
        ],
        "answer": 1
    }
]

# Constantes
TIME_LIMIT = 15  # segundos por pregunta

def main():
    st.title("📝 Quiz: Licencias Flexibles y Accesibles - MIT y BSD")

    if "score" not in st.session_state:
        st.session_state.score = 0
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    if "answered" not in st.session_state:
        st.session_state.answered = False

    q = questions[st.session_state.q_index]
    elapsed = time.time() - st.session_state.start_time
    remaining_time = max(0, TIME_LIMIT - int(elapsed))

    st.write(f"Pregunta {st.session_state.q_index + 1} de {len(questions)}")
    st.write(f"⏳ Tiempo restante: {remaining_time} segundos")

    if remaining_time == 0 and not st.session_state.answered:
        st.warning("Tiempo terminado. Pasando a la siguiente pregunta...")
        st.session_state.q_index += 1
        st.session_state.start_time = time.time()
        st.session_state.answered = False
        st.experimental_rerun()

    if not st.session_state.answered:
        option = st.radio(q["question"], q["options"], key=st.session_state.q_index)

        if st.button("Enviar respuesta"):
            st.session_state.answered = True
            time_taken = time.time() - st.session_state.start_time

            if q["options"].index(option) == q["answer"]:
                # Puntuación: 10 puntos base + bonus según rapidez
                bonus = max(0, TIME_LIMIT - time_taken)
                st.session_state.score += 10 + int(bonus)
                st.success(f"¡Correcto! Has ganado {10 + int(bonus)} puntos.")
            else:
                st.error("Respuesta incorrecta.")

            st.write(f"Respuesta correcta: {q['options'][q['answer']]}")

            if st.session_state.q_index + 1 < len(questions):
                if st.button("Siguiente pregunta"):
                    st.session_state.q_index += 1
                    st.session_state.start_time = time.time()
                    st.session_state.answered = False
                    st.experimental_rerun()
            else:
                st.write("¡Has completado el quiz!")
                st.write(f"Tu puntuación final es: **{st.session_state.score} puntos**")
    else:
        st.write("Por favor, pulsa 'Siguiente pregunta' para continuar.")

if __name__ == "__main__":
    main()
