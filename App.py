
import streamlit as st
import sqlite3
import pandas as pd
from datetime import date, datetime

DB = "sst.db"

def conn():
    return sqlite3.connect(DB, check_same_thread=False)

def init_db():
    c = conn()
    cur = c.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        senha TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cargo TEXT,
        setor TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS treinamentos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        funcionario_id INTEGER,
        treinamento TEXT,
        validade TEXT
    )
    """)

    cur.execute("INSERT OR IGNORE INTO usuarios(usuario,senha) VALUES('admin','admin123')")
    c.commit()
    c.close()

init_db()

st.set_page_config(page_title="SST 4.0", layout="wide")

if "logado" not in st.session_state:
    st.session_state.logado = False

def login():
    st.title("SST 4.0 - Login")
    u = st.text_input("Usuário")
    s = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        c = conn()
        cur = c.cursor()
        cur.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (u, s))
        if cur.fetchone():
            st.session_state.logado = True
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

if not st.session_state.logado:
    login()
    st.stop()

st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Opções",
    ["Dashboard", "Funcionários", "Treinamentos", "Usuários"]
)

if menu == "Dashboard":
    st.title("Dashboard SST")

    c = conn()

    total_func = pd.read_sql("SELECT * FROM funcionarios", c)
    total_trein = pd.read_sql("SELECT * FROM treinamentos", c)

    col1, col2 = st.columns(2)

    col1.metric("Funcionários", len(total_func))
    col2.metric("Treinamentos", len(total_trein))

    st.subheader("Funcionários")
    st.dataframe(total_func, use_container_width=True)

elif menu == "Funcionários":
    st.title("Cadastro de Funcionários")

    with st.form("func"):
        nome = st.text_input("Nome")
        cargo = st.text_input("Cargo")
        setor = st.text_input("Setor")

        if st.form_submit_button("Salvar"):
            c = conn()
            c.execute(
                "INSERT INTO funcionarios(nome,cargo,setor) VALUES(?,?,?)",
                (nome, cargo, setor)
            )
            c.commit()
            st.success("Funcionário cadastrado")

    c = conn()
    df = pd.read_sql("SELECT * FROM funcionarios", c)
    st.dataframe(df, use_container_width=True)

elif menu == "Treinamentos":
    st.title("Controle de Treinamentos")

    c = conn()
    funcionarios = pd.read_sql(
        "SELECT id,nome FROM funcionarios",
        c
    )

    if len(funcionarios) == 0:
        st.warning("Cadastre funcionários primeiro.")
    else:
        with st.form("trein"):
            func = st.selectbox(
                "Funcionário",
                funcionarios["nome"].tolist()
            )
            treinamento = st.text_input("Treinamento")
            validade = st.date_input("Validade", value=date.today())

            if st.form_submit_button("Salvar"):
                fid = int(
                    funcionarios.loc[
                        funcionarios["nome"] == func,
                        "id"
                    ].iloc[0]
                )

                c.execute(
                    """
                    INSERT INTO treinamentos
                    (funcionario_id,treinamento,validade)
                    VALUES (?,?,?)
                    """,
                    (fid, treinamento, str(validade))
                )
                c.commit()
                st.success("Treinamento cadastrado")

        consulta = pd.read_sql("""
        SELECT t.id,
               f.nome,
               t.treinamento,
               t.validade
        FROM treinamentos t
        JOIN funcionarios f
        ON f.id=t.funcionario_id
        """, c)

        st.dataframe(consulta, use_container_width=True)

        excel = consulta.to_csv(index=False).encode()
        st.download_button(
            "Exportar CSV",
            excel,
            "treinamentos.csv",
            "text/csv"
        )

elif menu == "Usuários":
    st.title("Cadastro de Usuários")

    with st.form("user"):
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")

        if st.form_submit_button("Cadastrar"):
            try:
                c = conn()
                c.execute(
                    "INSERT INTO usuarios(usuario,senha) VALUES(?,?)",
                    (usuario, senha)
                )
                c.commit()
                st.success("Usuário criado")
            except Exception as e:
                st.error(str(e))

    st.info("Usuário padrão: admin | Senha: admin123")
