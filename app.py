import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Sistema de Campamento MMSA",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CONFIG
# =========================
LOGO_PATH = "logo.png"
FONDO_PATH = "fondo.jpg"

USUARIO_VALIDO = "ADMIN"
CLAVE_VALIDA = "123"

# =========================
# FUNCIONES
# =========================
def img_to_base64(path):
    file_path = Path(path)
    if not file_path.exists():
        return ""
    return base64.b64encode(file_path.read_bytes()).decode()

def mostrar_login():
    logo_b64 = img_to_base64(LOGO_PATH)
    fondo_b64 = img_to_base64(FONDO_PATH)

    st.markdown(f"""
    <style>
    .stApp {{
        background:
            linear-gradient(rgba(10, 20, 35, 0.40), rgba(10, 20, 35, 0.52)),
            url("data:image/jpg;base64,{fondo_b64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background: transparent;
    }}

    [data-testid="stSidebar"] {{
        display: none;
    }}

    .login-container {{
        max-width: 520px;
        margin: 80px auto 30px auto;
        background: rgba(255,255,255,0.10);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255,255,255,0.22);
        border-radius: 26px;
        padding: 36px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
        text-align: center;
    }}

    .login-logo {{
        margin-bottom: 18px;
    }}

    .login-logo img {{
        max-width: 280px;
        background: rgba(255,255,255,0.96);
        border-radius: 18px;
        padding: 14px;
    }}

    .login-title {{
        font-size: 2.2rem;
        font-weight: 800;
        color: white;
        margin-bottom: 10px;
        text-shadow: 0 2px 12px rgba(0,0,0,0.25);
    }}

    .login-subtitle {{
        font-size: 1rem;
        color: rgba(255,255,255,0.96);
        margin-bottom: 10px;
        font-weight: 600;
        text-shadow: 0 2px 8px rgba(0,0,0,0.30);
    }}

    .input-label-fix {{
        color: #ffffff !important;
        font-weight: 700 !important;
        text-shadow: 0 2px 8px rgba(0,0,0,0.45);
        background: rgba(20, 28, 40, 0.38);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        padding: 6px 10px;
        border-radius: 10px;
        display: inline-block;
        margin-bottom: 6px;
    }}

    .stTextInput > div > div > input {{
        border-radius: 12px;
        background: rgba(255,255,255,0.95);
        color: #111827;
    }}

    .stButton > button {{
        width: 100%;
        border-radius: 14px;
        padding: 0.85rem 1rem;
        font-weight: 700;
        background: #ffffff;
        color: #162033;
        border: none;
        box-shadow: 0 8px 18px rgba(0,0,0,0.10);
    }}

    .stButton > button:hover {{
        background: #f4f6f8;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="login-container">
        <div class="login-logo">
            <img src="data:image/png;base64,{logo_b64}">
        </div>
        <div class="login-title">Sistema de Campamento</div>
        <div class="login-subtitle">mmsa.campamento@mansfieldmin.com</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1.4, 1])

    with c2:
        st.markdown('<div class="input-label-fix">Usuario</div>', unsafe_allow_html=True)
        usuario = st.text_input("", key="usuario_login", label_visibility="collapsed")

        st.markdown('<div class="input-label-fix">Contraseña</div>', unsafe_allow_html=True)
        clave = st.text_input("", type="password", key="clave_login", label_visibility="collapsed")

        if st.button("Ingresar"):
            if usuario == USUARIO_VALIDO and clave == CLAVE_VALIDA:
                st.session_state["login_ok"] = True
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")

def mostrar_panel():
    fondo_b64 = img_to_base64(FONDO_PATH)
    logo_b64 = img_to_base64(LOGO_PATH)

    st.markdown(f"""
    <style>
    .stApp {{
        background: #f2f4f8;
    }}

    [data-testid="stHeader"] {{
        background: rgba(255,255,255,0.75);
        backdrop-filter: blur(8px);
    }}

    section[data-testid="stSidebar"] {{
        background: #ffffff;
        border-right: 1px solid #e5e7eb;
    }}

    .sidebar-logo {{
        text-align: center;
        margin-bottom: 20px;
    }}

    .sidebar-logo img {{
        max-width: 210px;
    }}

    .main-banner {{
        background:
            linear-gradient(rgba(20, 30, 45, 0.35), rgba(20, 30, 45, 0.35)),
            url("data:image/jpg;base64,{fondo_b64}");
        background-size: cover;
        background-position: center;
        border-radius: 24px;
        padding: 34px;
        color: white;
        margin-bottom: 22px;
    }}

    .main-title {{
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 4px;
    }}

    .main-subtitle {{
        font-size: 1rem;
        opacity: 0.95;
    }}

    .card {{
        background: white;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.06);
        border: 1px solid #edf0f5;
    }}

    .card-label {{
        color: #6b7280;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 10px;
    }}

    .card-value {{
        color: #111827;
        font-size: 2.1rem;
        font-weight: 800;
        line-height: 1;
    }}

    .section-card {{
        background: white;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.06);
        border: 1px solid #edf0f5;
        min-height: 230px;
    }}

    .section-title {{
        font-size: 1.4rem;
        font-weight: 800;
        color: #111827;
        margin-bottom: 12px;
    }}

    .section-text {{
        color: #4b5563;
        line-height: 1.7;
        font-size: 1rem;
    }}

    .stButton > button {{
        border-radius: 12px;
    }}
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-logo">
            <img src="data:image/png;base64,{logo_b64}">
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Módulos")
        opcion = st.radio(
            "Ir a",
            ["Inicio", "Transporte", "Hotelería", "Personal", "Novedades", "Indicadores", "Configuración"],
            label_visibility="collapsed"
        )

        st.markdown("---")
        if st.button("Cerrar sesión"):
            st.session_state["login_ok"] = False
            st.rerun()

    st.markdown("""
    <div class="main-banner">
        <div class="main-title">Panel Principal</div>
        <div class="main-subtitle">Vista interna del sistema de campamento MMSA</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    datos = [
        ("Personal en sitio", "396"),
        ("Habitaciones ocupadas", "182"),
        ("Buses programados", "7"),
        ("Novedades activas", "5")
    ]

    for col, (label, value) in zip([c1, c2, c3, c4], datos):
        with col:
            st.markdown(f"""
            <div class="card">
                <div class="card-label">{label}</div>
                <div class="card-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    a, b = st.columns([1.2, 1])

    with a:
        st.markdown(f"""
        <div class="section-card">
            <div class="section-title">{opcion}</div>
            <div class="section-text">
                Este espacio corresponde al módulo <b>{opcion}</b>.
                <br><br>
                Acá luego vamos a cargar la lógica real del sistema, con tablas, filtros,
                formularios, indicadores y movimientos operativos.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">Accesos rápidos</div>
            <div class="section-text">
                • Movimientos del día<br>
                • Personal en tránsito<br>
                • Habitaciones disponibles<br>
                • Alertas activas<br>
                • KPIs operativos<br>
                • Novedades recientes
            </div>
        </div>
        """, unsafe_allow_html=True)

# =========================
# APP
# =========================
if "login_ok" not in st.session_state:
    st.session_state["login_ok"] = False

if st.session_state["login_ok"]:
    mostrar_panel()
else:
    mostrar_login()
