import streamlit as st

BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1470&q=80"

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
        .intro-card {{
            background: rgba(255, 255, 255, 0.9);
            padding: 25px 40px;
            border-radius: 20px;
            max-width: 700px;
            margin: 30px auto 20px auto;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #111;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
            text-align: justify;
            line-height: 1.5;
        }}
        .question-card {{
            background: rgba(255, 255, 255, 0.95);
            padding: 30px 50px;
            border-radius: 20px;
            box-shadow: 0 12px 48px 0 rgba(31, 38, 135, 0.7);
            max-width: 700px;
            margin: 20px auto 40px auto;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #111;
            text-align: center;
        }}
        .message {{
            margin-top: 20px;
            font-size: 18px;
            font-weight: 600;
        }}
        .success-message {{
            color: #2E8B57;
        }}
        .error-message {{
            color: #B22222;
        }}
        .block-container {{
            background-color: transparent !important;
            padding-top: 0px !important;
            padding-bottom: 0px !important;
        }}
        /* Opciones radio deshabilitadas */
        input[type="radio"]:disabled + label {{
            color: gray;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    set_bg()

    st.markdown(
        """
        <h1 style="text-align:center; color:#FFFAF0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            📝 Quiz: Licencias Flexibles y Accesibles - MIT y BSD
        </h1>
        <hr style="border: 2px solid #FFFAF0; border-radius: 5px; max-width: 700px; margin:auto;">
        """,
        unsafe_allow_html=True,
    )

    # Bloque introductorio para preparar al usuario
    st.markdown(
        """
        <div class="intro-card">
            <h2 style="text-align:center; color:#333;">Prepárate para el Quiz</h2>
            <p>
                Las licencias MIT y BSD son licencias de software de código abierto muy populares y flexibles. 
                Permiten a los desarrolladores usar, copiar, modificar y distribuir software con muy pocas restricciones, 
                fomentando la colaboración y el uso libre del código. La licencia MIT es conocida por su simplicidad, 
                mientras que BSD tiene varias variantes, algunas con cláusulas específicas que deben respetarse.
            </p>
            <p>
                Este quiz te ayudará a comprender mejor las características principales de estas licencias y su importancia 
                en el mundo del software abierto. ¡Buena suerte!
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "score" not in st.session_state:
        st.session_state.score = 0
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "selected_option_idx" not in st.session_state:
        st.session_state.selected_option_idx = None
    if "score_added" not in st.session_state:
        st.session_state.score_added = False

    q_index = st.session_state.q_index

    if q_index >= len(questions):
        st.balloons()
        st.markdown(
            f"""
            <div class="question-card">
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
            st.session_state.score_added = False
        return

    question = questions[q_index]

    st.markdown(f'<div class="question-card">', unsafe_allow_html=True)
    st.markdown(f'<h3 style="color:#333;">Pregunta {q_index + 1} de {len(questions)}</h3>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-weight:bold; color:#111; font-size:20px;">{question["question"]}</p>', unsafe_allow_html=True)

    if not st.session_state.answered:
        selected = st.radio(
            label="",
            options=question["options"],
            key="radio",
            index=0,
            help="Selecciona una opción"
        )
        if st.button("Enviar respuesta"):
            st.session_state.selected_option_idx = question["options"].index(selected)
            st.session_state.answered = True
    else:
        selected = st.radio(
            label="",
            options=question["options"],
            key="radio_disabled",
            index=st.session_state.selected_option_idx,
            disabled=True
        )
        if st.session_state.selected_option_idx == question["answer"]:
            if not st.session_state.score_added:
                st.session_state.score += 10
                st.session_state.score_added = True
            st.markdown(
                f'<p class="message success-message">✅ ¡Correcto! Has ganado 10 puntos.</p>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<p class="message error-message">❌ Respuesta incorrecta.</p>',
                unsafe_allow_html=True,
            )
        st.markdown(
            f"<p><b>Tu respuesta:</b> {question['options'][st.session_state.selected_option_idx]}</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<p><b>Respuesta correcta:</b> {question['options'][question['answer']]}</p>",
            unsafe_allow_html=True,
        )

        if st.button("Siguiente pregunta"):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.session_state.selected_option_idx = None
            st.session_state.score_added = False

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
