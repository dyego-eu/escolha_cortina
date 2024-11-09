from pathlib import Path
from PIL import Image
import numpy as np
import streamlit as st


def session_startup():
    st.session_state["startup"] = True
    st.session_state["cortinas"] = {
        "arvore_papiro": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "arvore_folhas_verdes_azuis": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "arvores": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "azul_bebe": {
            "has_2": True,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "azul_bebe_flores": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "azul_detalhes_dourados": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "azul_flores": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "azul_flores_amarelas": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "branca_detalhes_verdes": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "branca_flores_mais_verdes": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "branca_flores_verdes": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "dourada": {
            "has_2": True,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "folhinhas": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "flores_desenho": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "flores_passarinho": {
            "has_2": True,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "flores_vermelhas_caule_verde": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "marrom": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "pastel_flores": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "pastel_detalhes": {
            "has_2": True,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "pastel_samambaia": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "power_azul": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "prateada_brilhante": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "prateada_com_detalhes": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "prateada_com_flores": {
            "has_2": True,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "rosa": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "verde_cetim": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "verde_com_detalhes": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "verde_clarinho": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "verde_folhas": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "verde_inverno": {
            "has_2": True,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "vermelho_dourada": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
        "vermelho_quadriculado": {
            "has_2": False,
            "wins": 0,
            "total": 0,
            "win_rate": 0,
        },
    }
    st.session_state["cortina_names"] = np.array(list(st.session_state.cortinas.keys()))
    st.session_state.cortina_1, st.session_state.cortina_2 = np.random.choice(
        st.session_state.cortina_names, 2, replace=False
    )


if "startup" not in st.session_state:
    session_startup()

cortina_1, cortina_2 = st.session_state.cortina_1, st.session_state.cortina_2


images_folder = Path("images")

st.title("Escoja la mejor cortina")

if st.button("Ver resultados Parciais"):
    if not st.button("Esconder resultados Parciais"):
        for cortina in sorted(
            st.session_state.cortinas.keys(),
            key=lambda x: st.session_state.cortinas[x]["win_rate"],
            reverse=True,
        ):
            wins = st.session_state.cortinas[cortina]["wins"]
            total = st.session_state.cortinas[cortina]["total"]
            win_rate = st.session_state.cortinas[cortina]["win_rate"]

            st.markdown(
                f"[{cortina.replace('_', ' ').title()}](images/{cortina}.jpg): {wins}/{total} - {win_rate}"
            )

col1, col2 = st.columns([1, 1])

col1.header(cortina_1.replace("_", " ").title())
col1.image(Image.open(images_folder / f"{cortina_1}.jpg"))
if st.session_state.cortinas[cortina_1]["has_2"]:
    col1.image(Image.open(images_folder / f"{cortina_1}_2.jpg"))


col2.header(cortina_2.replace("_", " ").title())
col2.image(Image.open(images_folder / f"{cortina_2}.jpg"))
if st.session_state.cortinas[cortina_2]["has_2"]:
    col2.image(Image.open(images_folder / f"{cortina_2}_2.jpg"))


if col1.button("Esa es la mejor", key="mejor-1"):
    st.session_state.cortinas[cortina_1]["wins"] += 1
    st.session_state.cortinas[cortina_1]["total"] += 1
    st.session_state.cortinas[cortina_2]["total"] += 1
    st.session_state.cortinas[cortina_2]["win_rate"] = (
        st.session_state.cortinas[cortina_2]["wins"]
        / st.session_state.cortinas[cortina_2]["total"]
    )
    st.session_state.cortinas[cortina_1]["win_rate"] = (
        st.session_state.cortinas[cortina_1]["wins"]
        / st.session_state.cortinas[cortina_1]["total"]
    )
    st.session_state.cortina_1, st.session_state.cortina_2 = np.random.choice(
        st.session_state.cortina_names, 2, replace=False
    )
    st.rerun()


if col2.button("Esa es la mejor", key="mejor-2"):
    st.session_state.cortinas[cortina_2]["wins"] += 1
    st.session_state.cortinas[cortina_2]["total"] += 1
    st.session_state.cortinas[cortina_1]["total"] += 1

    st.session_state.cortinas[cortina_2]["win_rate"] = (
        st.session_state.cortinas[cortina_2]["wins"]
        / st.session_state.cortinas[cortina_2]["total"]
    )
    st.session_state.cortinas[cortina_1]["win_rate"] = (
        st.session_state.cortinas[cortina_1]["wins"]
        / st.session_state.cortinas[cortina_1]["total"]
    )
    st.session_state.cortina_1, st.session_state.cortina_2 = np.random.choice(
        st.session_state.cortina_names, 2, replace=False
    )
    st.rerun()
