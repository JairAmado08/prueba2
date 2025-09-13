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
    if "selected_option" not in st.session_state:
        st.session_state.selected_option = None
    if "show_next_button" not in st.session_state:
        st.session_state.show_next_button = False

    q_index = st.session_state.q_index

    if q_index >= len(questions):
        st.success("🎉 ¡Has completado el quiz!")
        st.write(f"Tu puntuación final es: **{st.session_state.score} puntos**")
        return

    question = questions[q_index]

    elapsed = time.time() - st.session_state.start_time
    remaining_time = TIME_LIMIT - int(elapsed)

    if remaining_time <= 0 and not st.session_state.answered:
        st.warning("⏰ Tiempo terminado para esta pregunta.")
        st.session_state.answered = True
        st.session_state.show_next_button = True

    st.write(f"Pregunta {q_index + 1} de {len(questions)}")
    st.write(f"⏳ Tiempo restante: {max(0, remaining_time)} segundos")

    if not st.session_state.answered:
        with st.form(key="quiz_form"):
            selected = st.radio(question["question"], question["options"])
            submit = st.form_submit_button("Enviar respuesta")

            if submit:
                st.session_state.selected_option = selected
                st.session_state.answered = True
                st.session_state.show_next_button = True

                time_taken = time.time() - st.session_state.start_time

                if question["options"].index(selected) == question["answer"]:
                    bonus = max(0, TIME_LIMIT - time_taken)
                    gained = 10 + int(bonus)
                    st.session_state.score += gained
                    st.success(f"¡Correcto! Has ganado {gained} puntos.")
                else:
                    st.error("Respuesta incorrecta.")

                st.write(f"Respuesta correcta: **{question['options'][question['answer']]}**")
    else:
        st.write(f"Tu respuesta: **{st.session_state.selected_option}**")
        st.write(f"Respuesta correcta: **{question['options'][question['answer']]}**")

    if st.session_state.show_next_button:
        if st.button("Siguiente pregunta"):
            st.session_state.q_index += 1
            st.session_state.start_time = time.time()
            st.session_state.answered = False
            st.session_state.selected_option = None
            st.session_state.show_next_button = False

if __name__ == "__main__":
    main()
