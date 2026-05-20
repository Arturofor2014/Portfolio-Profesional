import streamlit as st

st.set_page_config(
    page_title="Portfolio · Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

CANVA_URL = st.secrets.get("CANVA_URL", "")

# ── CHATBOT — RESPUESTAS ───────────────────────────────────────────────────────
RESPONSES = {
    "mmm":            "Hola espero estes bien, al momento solo respondo cosas basicas estoy aprendiendo naci hace pocos días. Ahora dime ¿en que te ayudo?", 
    "Hola":            "Hola espero estes bien", 
    "python":          "Tengo experiencia sólida en Python con pandas, NumPy, openpyxl, python-pptx, requests y Streamlit. Lo he usado para pipelines de extracción de datos desde PPTX y Excel, automatizar reportes financieros y desarrollar dashboards web.",
    "streamlit":       "He desarrollado dashboards web con Streamlit + Plotly integrados a Google Drive API, con autenticación, control de sesión (timeout 30 min), gráficas CAPEX interactivas y layout responsive para reportes ejecutivos.",
    "power bi":        "Manejo Power BI con Power Query, Power Pivot y DAX para dashboards de ventas, inventario y finanzas. También diseñé un Data Warehouse para migración a Power BI en JVLAT.",
    "excel":           "Excel avanzado: VBA, Power Query, Power Pivot, DAX. He automatizado plantillas financieras con openpyxl y pandas para portafolios multi-propiedad con 20+ inversiones.",
    "sql":             "Manejo SQL para consultas, extracción y transformación de datos en pipelines ETL y desarrollo de Data Warehouse.",
    "finanzas":        "Experiencia financiera en P&L, Balance General, Flujo de Caja, Business Plan, presupuestos y proyecciones. He calculado IRR, NPV, CAP Rate, Cash-on-Cash, Equity Multiple y ROI en portafolios inmobiliarios.",
    "irr":             "He calculado IRR, NPV, Equity Multiple, Cash-on-Cash, NIY y CAP Rate para portafolios de inversión inmobiliaria (Casco Antiguo y Santa Ana, 20+ propiedades).",
    "dashboard":       "He creado dashboards en Streamlit, Power BI y Excel con autenticación, gráficas Plotly interactivas y conexión en tiempo real a Google Drive API para reportes ejecutivos.",
    "experiencia":     "Experiencia:\n• Data Scientist – Casco Development & Partners (Oct 2025 – Presente)\n• Especialista Datamining – JVLAT (2024 – Mar 2025)\n• Analista Financiero – Varela Hermanos (2020 – 2024)\n• Analista BI – Mi Bus (2018 – 2019)\n• Analista Ventas – Huawei (2017 – 2018)",
    "varela":          "En Varela Hermanos (2020–2024): presupuestos, P&L, Flujo de Caja, KPIs de rentabilidad, liquidez y logística, reportes para gerencias y vicepresidencias.",
    "huawei":          "En Huawei Technologies (2017–2018): pronóstico cuatrimestral, cálculo de incentivos, análisis de impacto por inventario y posicionamiento A/B/C/D de producto.",
    "mi bus":          "En Mi Bus (2018–2019): reportes en Excel, Power BI y R para inventario, compras y control operativo.",
    "jvlat":           "En JVLAT (2024 – Marzo 2025): análisis B2B Sell In/Out, Trade y Warehouse para Chile, Colombia y Perú, segmentación de clientes y Data Warehouse para Power BI.",
    "casco":           "En Casco Development & Partners (Oct 2025 – Presente): pipelines Python para extracción de métricas desde PPTX, dashboards Streamlit + Google Drive y automatización Excel para 20+ inversiones.",
    "educacion":       "Formación:\n• Especialización en Econometría Aplicada (2023 – Presente)\n• Maestría en Banca y Finanzas – Univ. del Istmo (2020 – Presente)\n• Ingeniería Industrial – UIP (2008 – 2015)\n• Bachiller en Ciencias – Instituto América",
    "maestria":        "Maestría en Banca y Finanzas – Universidad del Istmo (2020 – Presente) y Especialización en Econometría Aplicada y Análisis de Datos.",
    "econometria":     "Especialización en Econometría Aplicada con RStudio, STATA, Python, SPSS y MATLAB.",
    "habilidades":     "Habilidades:\n• Lenguajes: Python, R, SQL, VBA, DAX, JS, HTML, CSS\n• BI: Power BI, Streamlit, Plotly, Power Query\n• Data Eng: ETL, Data Warehouse, Google Drive API\n• ML: Scikit-learn, STATA, SPSS, MATLAB\n• Finanzas: IRR, NPV, P&L, CAPEX, Equity Multiple",
    "stack":           "Stack: Python · Streamlit · Plotly · pandas · openpyxl · python-pptx · Google Drive API · Power BI · SQL · R · Excel · DAX · VBA.",
    "machine learning":"Conocimientos en Machine Learning con Scikit-learn, estadística avanzada con STATA, SPSS y MATLAB.",
    "proyecto":        "Proyectos:\n• Dashboard Estado de Resultado (P&L)\n• Closing Dashboard – proyectos inmobiliarios\n• Cash Flow – flujo de caja\n• Cuadro de Mando Financiero\n• Portafolio interactivo con chatbot",
    "google":          "He trabajado con Google Drive API para integración de datos en tiempo real en dashboards Streamlit y Google Sheets como fuente de datos para reportes automatizados.",
    "idioma":          "Español nativo e inglés intermedio.",
    "ingles":          "Inglés intermedio — lectura técnica fluida, comunicación escrita y oral básica-intermedia.",
}

def get_response(user_input: str) -> str:
    text = user_input.lower()
    for keyword, response in RESPONSES.items():
        if keyword in text:
            return response
    return "No tengo información sobre eso. Puedes preguntarme sobre: experiencia, habilidades, Python, Power BI, finanzas, dashboards, proyectos o educación."

with st.sidebar:
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0A2463,#1E5FA8);
         padding:14px 16px;border-radius:10px;margin-bottom:12px;">
        <div style="color:white;font-size:15px;font-weight:900;">🤖 Pregúntame</div>
        <div style="color:#D6E4F7;font-size:11px;">Sobre experiencia y habilidades</div>
    </div>
    """, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "bot", "content": "¡Hola! Pregúntame sobre experiencia, habilidades, proyectos o formación."}
        ]

    if st.button("🗑️ Limpiar chat", use_container_width=True):
        st.session_state.messages = [
            {"role": "bot", "content": "¡Hola! Pregúntame sobre experiencia, habilidades, proyectos o formación."}
        ]
        st.rerun()

    # Mostrar historial
    for m in st.session_state.messages:
        if m["role"] == "user":
            with st.chat_message("user"):
                st.write(m["content"])
        else:
            with st.chat_message("assistant"):
                st.write(m["content"])

    # Input
    question = st.chat_input("Escribe tu pregunta...")
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        answer = get_response(question)
        st.session_state.messages.append({"role": "bot", "content": answer})
        st.rerun()

# ── ESTILOS GLOBALES ───────────────────────────────────────────────────────────
st.markdown("""
<style>
.main .block-container { max-width: 1300px; padding: 1.5rem 2rem; }

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

.project-card {
    background: white; border-radius: 12px;
    padding: 20px; margin-bottom: 16px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    border-left: 4px solid #0A2463;
    transition: transform 0.2s;
}
.project-card:hover { transform: translateY(-2px); box-shadow: 0 4px 16px rgba(0,0,0,0.12); }
.project-title { font-size: 15px; font-weight: 800; color: #0A2463; margin-bottom: 6px; }
.project-desc  { font-size: 12.5px; color: #555; line-height: 1.6; margin-bottom: 12px; }
.project-tags  { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.tag {
    background: #EFF3FA; color: #0A2463;
    font-size: 11px; font-weight: 600;
    padding: 3px 10px; border-radius: 20px;
}
.project-link {
    display: inline-block; background: #0A2463; color: white !important;
    font-size: 12px; font-weight: 700; padding: 7px 16px;
    border-radius: 6px; text-decoration: none;
}
.project-link:hover { background: #1E5FA8; }

.sec-header {
    background: #0A2463; color: white;
    padding: 10px 16px; border-radius: 8px;
    font-size: 13px; font-weight: 800;
    letter-spacing: 0.5px; margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# ── HEADER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="portfolio-header">
    <div class="portfolio-title">📊 Portfolio Profesional</div>
    <div class="portfolio-sub">Data Scientist &amp; Financial Analytics Engineer</div>
</div>
""", unsafe_allow_html=True)

# ── TABS ───────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["🗂️  Portafolio", "📄  Hoja de Vida"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1: PORTAFOLIO
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown('<div class="sec-header">🚀 Proyectos Desarrollados</div>', unsafe_allow_html=True)

    projects = [
        {
            "title": "Estado de Resultado — Dashboard P&L",
            "desc": "Dashboard financiero interactivo para análisis de Estado de Resultados. Visualización de ingresos, costos, gastos y utilidades con comparativo real vs presupuesto.",
            "tags": ["Python", "Streamlit", "Plotly", "Finanzas", "P&L"],
            "url": "https://estado-de-resultado-j2xcmkofq7q7zwnqs9ycmu.streamlit.app/",
        },
        {
            "title": "Closing Dashboard — Cierre de Proyectos",
            "desc": "Sistema de seguimiento de cierre de proyectos inmobiliarios. Monitoreo de métricas clave, cronogramas y estados de entrega en tiempo real.",
            "tags": ["Python", "Streamlit", "Google Drive API", "Inmobiliario"],
            "url": "https://closing-ydh6wy5habve4kbgqchkep.streamlit.app/",
        },
        {
            "title": "Cash Flow — Flujo de Caja",
            "desc": "Herramienta de análisis y proyección de flujo de caja. Visualización de entradas, salidas y saldo neto con proyecciones y escenarios financieros.",
            "tags": ["Python", "Streamlit", "Plotly", "Flujo de Caja", "Finanzas"],
            "url": "https://cashflow-rnqmupyaqzpdva42uw6ywt.streamlit.app/",
        },
        {
            "title": "Cuadro de Mando Financiero",
            "desc": "Dashboard ejecutivo con indicadores clave de desempeño financiero. Consolidación de métricas de rentabilidad, liquidez y solvencia para toma de decisiones gerenciales.",
            "tags": ["Python", "Streamlit", "Plotly", "KPIs", "Google Drive API"],
            "url": "https://cuadro-de-mando-financiero-m5kczw8rezx8fx8dvfcz8z.streamlit.app/",
        },
    ]

    col1, col2 = st.columns(2)
    for i, p in enumerate(projects):
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
        card = f"""
        <div class="project-card">
            <div class="project-title">{p['title']}</div>
            <div class="project-desc">{p['desc']}</div>
            <div class="project-tags">{tags_html}</div>
            <a class="project-link" href="{p['url']}" target="_blank">🔗 Ver proyecto</a>
        </div>
        """
        with col1 if i % 2 == 0 else col2:
            st.markdown(card, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="sec-header">📄 Hoja de Vida</div>', unsafe_allow_html=True)
    if CANVA_URL:
        st.markdown(f"""
        <a href="{CANVA_URL}" target="_blank"
           style="display:inline-block;background:#0A2463;color:white;font-weight:700;
                  font-size:14px;padding:12px 28px;border-radius:8px;text-decoration:none;
                  box-shadow:0 2px 8px rgba(0,0,0,0.2);">
           🔗 Ver Hoja de Vida en Canva
        </a>
        """, unsafe_allow_html=True)
    else:
        st.info("Configura CANVA_URL en Secrets.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2: HOJA DE VIDA
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    col_left, col_right = st.columns([1, 1.6])

    with col_left:
        st.markdown('<div class="sec-header">👤 Perfil</div>', unsafe_allow_html=True)
        st.markdown("""
        Data Scientist con perfil híbrido que combina **análisis financiero avanzado**,
        **automatización de pipelines de datos** y **desarrollo de dashboards interactivos**.
        Especializado en soluciones end-to-end desde extracción de datos hasta
        visualización ejecutiva en Streamlit y Power BI.
        """)

        st.markdown('<div class="sec-header" style="margin-top:16px;">🛠️ Habilidades</div>', unsafe_allow_html=True)
        skills = {
            "🐍 Lenguajes": "Python · R · SQL · VBA · DAX · JavaScript · HTML · CSS",
            "📊 BI & Viz": "Power BI · Streamlit · Plotly · Power Query · Power Pivot · Canva",
            "⚙️ Data Eng.": "ETL · Data Warehouse · Google Drive API · openpyxl · python-pptx",
            "🤖 ML & Stats": "Scikit-learn · Econometría · STATA · SPSS · MATLAB",
            "💰 Finanzas": "IRR · NPV · P&L · CAPEX · Equity Multiple · Flujo de Caja",
        }
        for cat, val in skills.items():
            st.markdown(f"**{cat}**")
            st.markdown(f"<small style='color:#555;'>{val}</small>", unsafe_allow_html=True)
            st.markdown("")

        st.markdown('<div class="sec-header" style="margin-top:8px;">🎓 Educación</div>', unsafe_allow_html=True)
        edus = [
            ("Especialización en Econometría Aplicada y Análisis de Datos", "2023 – Presente"),
            ("Maestría en Banca y Finanzas · Universidad del Istmo", "2020 – Presente"),
            ("Ingeniería Industrial y Sistemas · UIP", "2008 – 2015"),
            ("Bachiller en Ciencias · Instituto América", "Secundaria"),
        ]
        for titulo, fecha in edus:
            st.markdown(f"**{titulo}**")
            st.markdown(f"<small style='color:#888;'>{fecha}</small>", unsafe_allow_html=True)
            st.markdown("")

    with col_right:
        st.markdown('<div class="sec-header">💼 Experiencia</div>', unsafe_allow_html=True)
        jobs = [
            {
                "title": "Data Scientist & Financial Automation Specialist",
                "org": "Casco Development & Partners",
                "date": "Oct 2025 – Presente",
                "bullets": [
                    "Pipelines Python para extracción automática de métricas financieras (IRR, NPV, Equity Multiple, Cash-on-Cash, NIY) desde presentaciones PowerPoint multi-proyecto.",
                    "Dashboards web (Streamlit + Plotly) integrados a Google Drive API con KPIs en tiempo real, autenticación y gráficas CAPEX interactivas.",
                    "Automatización de plantillas Excel (openpyxl/pandas) para portafolios multi-propiedad con 20+ inversiones.",
                    "Extracción y normalización de datos desde PPTX con manejo de celdas combinadas para reporting ejecutivo de juntas directivas.",
                ]
            },
            {
                "title": "Especialista de Datamining & Reporting",
                "org": "Juegos de Video Latinoamérica (JVLAT)",
                "date": "2024 – Marzo 2025",
                "bullets": [
                    "Análisis B2B: Sell In, Sell Out, Trade y Warehouse — Chile, Colombia y Perú.",
                    "Diseño y desarrollo de Data Warehouse para migración a Power BI.",
                    "Dashboards interactivos de rendimiento comercial.",
                ]
            },
            {
                "title": "Analista de Planificación Financiera",
                "org": "Varela Hermanos",
                "date": "2020 – 2024  (4 años 6 meses)",
                "bullets": [
                    "Modelos financieros: P&L, Flujo de Caja, Balance General, Mix de Producto.",
                    "KPIs de rentabilidad, liquidez, solvencia, inventario y logística.",
                    "Reportes y presentaciones para gerencias y vicepresidencias.",
                ]
            },
            {
                "title": "Analista de Inteligencia de Negocio",
                "org": "Transporte Masivo Mi Bus",
                "date": "2018 – 2019",
                "bullets": ["Reportes en Excel, Power BI y R para inventario, compras y operaciones."]
            },
            {
                "title": "Analista de Ventas",
                "org": "Huawei Technologies",
                "date": "2017 – 2018",
                "bullets": ["Pronóstico cuatrimestral, cálculo de incentivos y análisis de competidores."]
            },
        ]
        for j in jobs:
            bullets_html = "".join(
                f"<div style='font-size:12px;color:#333;margin-bottom:3px;'>• {b}</div>"
                for b in j["bullets"]
            )
            st.markdown(f"""
            <div style="border-left:3px solid #0A2463;padding-left:12px;margin-bottom:18px;">
                <div style="font-weight:800;color:#0A2463;font-size:14px;">{j['title']}</div>
                <div style="color:#1E5FA8;font-size:12px;font-style:italic;">{j['org']}</div>
                <div style="color:#888;font-size:11px;margin-bottom:6px;">{j['date']}</div>
                {bullets_html}
            </div>
            """, unsafe_allow_html=True)

