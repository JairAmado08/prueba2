import streamlit as st

# Imagen de fondo
BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1470&q=80"

# Preguntas
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

# Estilos visuales
def set_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{BACKGROUND_IMAGE}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .question-card {{
            background: rgba(255, 255, 255, 0.92);
            padding: 25px 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px 0 rgba(31, 38, 135, 0.5);
            max-width: 700px;
            margin: 30px auto;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #111;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Lógica principal
def main():
    set_bg()

    st.markdown(
        """
        <h1 style="text-align:center; color:#FFFAF0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            📝 Quiz: Licencias Flexibles y Accesibles - MIT y BSD
        </h1>
        <hr style="border: 2px solid #FFFAF0; border-radius: 5px;">
        """,
        unsafe_allow_html=True,
    )

    # Estado de la app
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "selected_option_idx" not in st.session_state:
        st.session_state.selected_option_idx = None
    if "show_next_button" not in st.session_state:
        st.session_state.show_next_button = False

    q_index = st.session_state.q_index

    # Mostrar resultado final
    if q_index >= len(questions):
        st.balloons()
        st.markdown(
            f"""
            <div class="question-card" style="text-align:center;">
                <h2 style="color:#2E8B57;">🎉 ¡Has completado el quiz!</h2>
                <h3 style="color:#1E90FF;">Tu puntuación final es: <strong>{st.session_state.score} puntos</strong></h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("🔄 Reiniciar quiz"):
            st.session_state.score = 0
            st.session_state.q_index = 0
            st.session_state.answered = False
            st.session_state.selected_option_idx = None
            st.session_state.show_next_button = False
        return

    question = questions[q_index]

    # Cuadro de pregunta
    st.markdown(f'<div class="question-card">', unsafe_allow_html=True)
    st.markdown(f'<h3 style="color:#333;">Pregunta {q_index + 1} de {len(questions)}</h3>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-weight:bold; color:#111; font-size:18px;">{question["question"]}</p>', unsafe_allow_html=True)

    # Mostrar opciones y procesar respuesta
    if not st.session_state.answered:
        with st.form(key="quiz_form"):
            selected = st.radio("", question["options"], key="radio")
            submit = st.form_submit_button("Enviar respuesta")
            if submit:
                st.session_state.selected_option_idx = question["options"].index(selected)
                st.session_state.answered = True
                st.session_state.show_next_button = True

                if st.session_state.selected_option_idx == question["answer"]:
                    st.success("✅ ¡Correcto! Has ganado 10 puntos.")
                    st.session_state.score += 10
                else:
                    st.error("❌ Respuesta incorrecta.")

                st.markdown(
                    f"<p><b>Respuesta correcta:</b> {question['options'][question['answer']]}</p>",
                    unsafe_allow_html=True,
                )
    else:
        # Mostrar solo respuestas, sin permitir cambiar
        st.markdown(
            f"<p><b>Tu respuesta:</b> {question['options'][st.session_state.selected_option_idx]}</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<p><b>Respuesta correcta:</b> {question['options'][question['answer']]}</p>",
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # Botón para siguiente pregunta
    if st.session_state.show_next_button:
        if st.button("Siguiente pregunta", key="next_btn"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.session_state.selected_option_idx = None
            st.session_state.show_next_button = False

# Ejecutar
if __name__ == "__main__":
    main()
