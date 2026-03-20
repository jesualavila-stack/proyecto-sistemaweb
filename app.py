import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Sistema de Campamento MMSA",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================
# CONFIG
# =========================
APP_TITLE = "Sistema de Campamento"
# Mantener la portada/login premium actual sin cambios.
# Este archivo apunta a mejorar solamente la vista interna luego del ingreso.
APP_SUBTITLE = "Mansfield Minera S.A."
USER_NAME = "ADMIN"

BACKGROUND_IMAGE = "fondo_mina.jpg"   # Cambiar por tu archivo real
LOGO_IMAGE = "logo_mmsa.png"          # Cambiar por tu archivo real

MENU = [
    ("Inicio", "🏠"),
    ("Transporte", "🚌"),
    ("Hotelería", "🛏️"),
    ("Personal", "👷"),
    ("Novedades", "📢"),
    ("Indicadores", "📊"),
    ("Configuración", "⚙️"),
]

# =========================
# HELPERS
# =========================
def img_to_base64(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        return ""
    return base64.b64encode(file_path.read_bytes()).decode()

bg_b64 = img_to_base64(BACKGROUND_IMAGE)
logo_b64 = img_to_base64(LOGO_IMAGE)

if "menu_activo" not in st.session_state:
    st.session_state.menu_activo = "Inicio"

# =========================
# STYLES
# =========================
st.markdown(
    f"""
    <style>
    :root {{
        --sidebar-bg: rgba(10, 22, 45, 0.92);
        --card-bg: rgba(255, 255, 255, 0.80);
        --glass-bg: rgba(255, 255, 255, 0.14);
        --glass-border: rgba(255, 255, 255, 0.20);
        --text-main: #ffffff;
        --text-dark: #162033;
        --muted: #6b7280;
        --accent: #dce9f7;
        --shadow: 0 12px 30px rgba(0,0,0,0.18);
        --radius: 22px;
    }}

    .stApp {{
        background:
            linear-gradient(rgba(7, 15, 30, 0.22), rgba(7, 15, 30, 0.35)),
            url("data:image/jpg;base64,{bg_b64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, rgba(10,22,45,0.96) 0%, rgba(8,18,38,0.92) 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }}

    [data-testid="stSidebar"] * {{
        color: white !important;
    }}

    .sidebar-logo-wrap {{
        background: rgba(255,255,255,0.96);
        border-radius: 18px;
        padding: 14px;
        margin-top: 8px;
        margin-bottom: 18px;
        box-shadow: var(--shadow);
        text-align: center;
    }}

    .sidebar-logo-wrap img {{
        max-width: 100%;
        height: auto;
    }}

    .sidebar-title {{
        font-size: 1.08rem;
        font-weight: 700;
        margin-top: 6px;
        margin-bottom: 2px;
        color: #ffffff;
    }}

    .sidebar-subtitle {{
        font-size: 0.86rem;
        color: rgba(255,255,255,0.72);
        margin-bottom: 16px;
    }}

    .section-label {{
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: .08em;
        color: rgba(255,255,255,0.62);
        margin-top: 10px;
        margin-bottom: 10px;
        font-weight: 700;
    }}

    .menu-spacer {{
        height: 6px;
    }}

    .hero-wrap {{
        padding: 8px 6px 2px 6px;
        margin-bottom: 10px;
    }}

    .hero-title {{
        font-size: 2.2rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0.25rem;
        text-shadow: 0 2px 12px rgba(0,0,0,0.20);
    }}

    .hero-subtitle {{
        font-size: 1rem;
        color: rgba(255,255,255,0.90);
        margin-bottom: 1.2rem;
    }}

    .glass-card {{
        background: var(--card-bg);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: var(--radius);
        padding: 20px 22px;
        box-shadow: var(--shadow);
        min-height: 132px;
    }}

    .metric-label {{
        color: #4b5563;
        font-size: 0.95rem;
        margin-bottom: 10px;
        font-weight: 600;
    }}

    .metric-value {{
        color: var(--text-dark);
        font-size: 2.35rem;
        font-weight: 800;
        line-height: 1;
        margin-bottom: 4px;
    }}

    .metric-foot {{
        color: #6b7280;
        font-size: 0.84rem;
    }}

    .content-card {{
        background: rgba(255,255,255,0.78);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255,255,255,0.24);
        border-radius: 24px;
        padding: 24px;
        box-shadow: var(--shadow);
        min-height: 260px;
    }}

    .content-title {{
        color: #172033;
        font-size: 1.7rem;
        font-weight: 800;
        margin-bottom: 10px;
    }}

    .content-text {{
        color: #374151;
        font-size: 1rem;
        line-height: 1.7;
    }}

    div.stButton > button {{
        width: 100%;
        border-radius: 14px;
        padding: 0.7rem 1rem;
        border: 1px solid rgba(255,255,255,0.08);
        background: rgba(255,255,255,0.08);
        color: #ffffff;
        font-weight: 600;
        transition: all .2s ease;
    }}

    div.stButton > button:hover {{
        border: 1px solid rgba(255,255,255,0.16);
        background: rgba(255,255,255,0.14);
        transform: translateY(-1px);
    }}

    .active-menu div.stButton > button {{
        background: rgba(255,255,255,0.18) !important;
        border: 1px solid rgba(255,255,255,0.24) !important;
        box-shadow: inset 0 0 0 1px rgba(255,255,255,0.06);
    }}

    .logout-wrap {{
        margin-top: 20px;
        padding-top: 12px;
        border-top: 1px solid rgba(255,255,255,0.08);
    }}

    .quick-badge {{
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        background: rgba(22, 32, 51, 0.08);
        color: #172033;
        font-size: 0.82rem;
        font-weight: 700;
        margin-bottom: 10px;
    }}

    .block-container {{
        padding-top: 2.2rem;
        padding-bottom: 1.5rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    if logo_b64:
        st.markdown(
            f"""
            <div class="sidebar-logo-wrap">
                <img src="data:image/png;base64,{logo_b64}">
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="sidebar-logo-wrap"><b>LOGO MMSA</b></div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-title">Sistema de Campamento</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Versión premium MMSA</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Módulos</div>', unsafe_allow_html=True)

    for nombre, icono in MENU:
        active_class = "active-menu" if st.session_state.menu_activo == nombre else ""
        st.markdown(f'<div class="{active_class}">', unsafe_allow_html=True)
        if st.button(f"{icono}  {nombre}", key=f"menu_{nombre}"):
            st.session_state.menu_activo = nombre
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="logout-wrap">', unsafe_allow_html=True)
    st.button("Cerrar sesión", key="logout")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# IMPORTANTE
# =========================
# Esta maqueta corresponde SOLO al sistema luego de iniciar sesión.
# La portada de acceso premium debe conservarse igual a como ya la tenías.
# En tu proyecto final, este bloque debe renderizarse únicamente cuando:
# st.session_state.get("authenticated") == True

# =========================
# MAIN HEADER
# =========================
st.markdown(
    f"""
    <div class="hero-wrap">
        <div class="hero-title">Panel Principal</div>
        <div class="hero-subtitle">Versión premium del sistema de campamento MMSA</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================
# METRICS
# =========================
col1, col2, col3, col4 = st.columns(4, gap="medium")

metric_data = [
    ("Personal en sitio", "396", "Actualizado al momento"),
    ("Habitaciones ocupadas", "182", "Incluye dobles y fijas"),
    ("Buses programados", "7", "Próxima salida operativa"),
    ("Novedades activas", "5", "Pendientes de revisión"),
]

for col, (label, value, foot) in zip([col1, col2, col3, col4], metric_data):
    with col:
        st.markdown(
            f"""
            <div class="glass-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-foot">{foot}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

# =========================
# CONTENT AREA
# =========================
left, right = st.columns([1.25, 1], gap="large")

with left:
    st.markdown(
        """
        <div class="content-card">
            <div class="quick-badge">Resumen operativo</div>
            <div class="content-title">Una vista más limpia, moderna y profesional</div>
            <div class="content-text">
                Este diseño prioriza legibilidad, jerarquía visual y sensación premium.
                Se redujo el ruido visual, se mejoró el contraste y las tarjetas ahora tienen
                una estética tipo glassmorphism suave, sin perder la imagen de fondo del campamento.
                <br><br>
                La idea es que el sistema se vea corporativo, simple de usar y escalable para futuros módulos.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="content-card">
            <div class="quick-badge">Accesos rápidos</div>
            <div class="content-title">Próximos pasos recomendados</div>
            <div class="content-text">
                • Tarjetas clickeables por módulo<br>
                • Tabla de movimientos recientes<br>
                • Panel real de KPIs<br>
                • Buscador global de personal<br>
                • Alertas visuales y notificaciones<br>
                • Modo oscuro corporativo uniforme
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

# =========================
# MODULE PREVIEW
# =========================
st.markdown(
    f"""
    <div class="content-card" style="min-height: 180px;">
        <div class="quick-badge">Módulo activo</div>
        <div class="content-title">{st.session_state.menu_activo}</div>
        <div class="content-text">
            Aquí luego podemos cargar el contenido real del módulo seleccionado.
            Este rediseño está pensado únicamente para la interfaz posterior al login,
            manteniendo intacta la portada premium de acceso.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
