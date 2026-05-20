import streamlit as st
from chatbot import get_response

# ── CONFIG ─────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Portfolio · Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── ESTILOS ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
.main .block-container { max-width: 1300px; padding: 1.5rem 2rem; }
section[data-testid="stSidebar"] { display: none; }

.portfolio-header {
    background: linear-gradient(135deg, #0A2463 0%, #1E5FA8 100%);
    padding: 28px 36px; border-radius: 14px; margin-bottom: 24px;
}
.portfolio-title { color: white; font-size: 28px; font-weight: 900; letter-spacing: 1px; }
.portfolio-sub   { color: #D6E4F7; font-size: 14px; margin-top: 4px; }

.stTabs [data-baseweb="tab-list"] { gap: 8px; border-bottom: 2px solid #E0E0E0; }
.stTabs [data-baseweb="tab"] {
    font-weight: 600; font-size: 14px;
    padding: 10px 20px; border-radius: 8px 8px 0 0; color: #555;
}
.stTabs [aria-selected="true"] { background:#0A2463 !important; color:white !important; }

.chat-box {
    background: #F4F6FB; border-radius: 12px;
    padding: 16px; height: 440px; overflow-y: auto;
    margin-bottom: 12px; border: 1px solid #e0e0e0;
}
.msg-user {
    background: #0A2463; color: white;
    padding: 10px 14px; border-radius: 12px 12px 2px 12px;
    margin: 6px 0 6px 20%; font-size: 13px; line-height: 1.5;
}
.msg-bot {
    background: white; color: #1A1A2E;
    padding: 10px 14px; border-radius: 12px 12px 12px 2px;
    margin: 6px 20% 6px 0; font-size: 13px; line-height: 1.5;
    border: 1px solid #e0e0e0; box-shadow: 0 1px 4px rgba(0,0,0,0.07);
}
.lbl-u { font-size:11px; color:#0A2463; text-align:right; font-weight:700; margin-bottom:2px; }
.lbl-b { font-size:11px; color:#555; font-weight:700; margin-bottom:2px; }
</style>
""", unsafe_allow_html=True)

# ── CANVA URL (pon aquí tu link público de Canva) ──────────────────────────────
CANVA_URL = st.secrets.get("CANVA_URL", "")

# ── HEADER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="portfolio-header">
    <div class="portfolio-title">📊 Portfolio Profesional</div>
    <div class="portfolio-sub">Data Scientist &amp; Financial Analytics Engineer</div>
</div>
""", unsafe_allow_html=True)

# ── TABS ───────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["🖼️  Presentación", "🤖  Chatbot — Pregúntame"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1: CANVA
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("#### Navega la presentación directamente aquí")
    if CANVA_URL:
        st.markdown(f"""
        <div style="width:606px;height:567px;
             box-shadow:0 2px 8px 0 rgba(63,69,81,0.16);margin-bottom:0.9em;
             overflow:hidden;border-radius:8px;">
          <iframe loading="lazy"
            style="width:100%;height:100%;border:none;padding:0;margin:0;"
            src="{CANVA_URL}"
            allowfullscreen="allowfullscreen" allow="fullscreen">
          </iframe>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("⚙️ Agrega el link público de Canva en `.streamlit/secrets.toml` → `CANVA_URL = '...'`")
        st.markdown("""
        **Cómo obtener el link en Canva:**
        1. Abre tu presentación
        2. Clic en **Compartir**
        3. **Publicar como sitio web** o **Insertar**
        4. Copia el link generado
        """)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2: CHATBOT
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    col_chat, col_info = st.columns([2, 1])

    with col_info:
        st.markdown("#### ¿Qué puedes preguntar?")
        st.markdown("""
        - 💼 Experiencia laboral
        - 🛠️ Habilidades técnicas
        - 📊 Proyectos desarrollados
        - 🎓 Educación y formación
        - 🐍 Stack tecnológico
        - 💰 Conocimiento financiero
        """)
        st.divider()
        st.markdown("**Ejemplos rápidos:**")
        examples = [
            "¿Qué experiencia tienes en Python?",
            "¿Cuál es tu stack tecnológico?",
            "¿Has trabajado con dashboards?",
            "¿Qué proyectos has desarrollado?",
            "¿Tienes experiencia financiera?",
            "¿Qué estudios tienes?",
        ]
        for ex in examples:
            if st.button(ex, use_container_width=True, key=ex):
                st.session_state.setdefault("messages", [])
                st.session_state["pending"] = ex

    with col_chat:
        st.markdown("#### Escribe tu pregunta")

        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "bot",
                 "content": "¡Hola! Puedes preguntarme sobre experiencia, habilidades, proyectos o formación. ¿En qué te puedo ayudar?"}
            ]

        # Render chat
        html = '<div class="chat-box">'
        for m in st.session_state.messages:
            if m["role"] == "user":
                html += f'<div class="lbl-u">Tú</div><div class="msg-user">{m["content"]}</div>'
            else:
                content = m["content"].replace("\n", "<br>")
                html += f'<div class="lbl-b">🤖 Asistente</div><div class="msg-bot">{content}</div>'
        html += '</div>'
        st.markdown(html, unsafe_allow_html=True)

        user_input = st.chat_input("Escribe aquí tu pregunta...")
        question = user_input or st.session_state.pop("pending", None)

        if question:
            st.session_state.messages.append({"role": "user", "content": question})
            answer = get_response(question)
            st.session_state.messages.append({"role": "bot", "content": answer})
            st.rerun()
