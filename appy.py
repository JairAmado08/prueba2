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
        .question-card {{
            background: rgba(255, 255, 255, 0.9);
            padding: 25px 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px 0 rgba(31, 38, 135, 0.5);
            max-width: 700px;
            margin: 30px auto 30px auto;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #111;
        }}
        .btn-next {{
            background-color: #4CAF50;
            color: white;
            padding: 12px 25px;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 20px;
        }}
        .btn-next:hover {{
            background-color: #45a049;
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
        <hr style="border: 2px solid #FFFAF0; border-radius: 5px;">
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
    if "show_next_button" not in st.session_state:
        st.session_state.show_next_button = False

    q_index = st.session_state.q_index

    if q_index >= len(questions):
        st.balloons()
        st.markdown(
            f"""
            <div class="question-card" style="text-align:center;">
                <h2 style="color:#2E8B57;">🎉 ¡H
