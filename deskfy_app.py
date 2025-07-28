# requirements.txt:
# streamlit
# pandas
# requests
# openpyxl

import streamlit as st
import pandas as pd
import requests
from io import BytesIO
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
import json
import hashlib

st.set_page_config(page_title="Deskfy API - Exportação", layout="centered")
st.title("Deskfy API - Consulta e Exportação")

with st.sidebar:
    st.header("Credenciais e Configuração")
    st.session_state.api_key = "47200d78-1f10-44ba-a8e4-187a7d35e3bd"
    st.markdown(":white_check_mark: API Key carregada com sucesso.")

if "consultas_salvas" not in st.session_state:
    st.session_state.consultas_salvas = {}

# Definição das listas tabela_ordem e CAMPOS_BEBIDAS mantida como antes...
# Definição das funções dict_flatten, formatar_excel e exibir_tabela_formatada mantida como antes...

opcao = st.radio("Selecione a operação:", ["Consultar Relatórios", "Consultar Detalhes da Solicitação"])

if opcao == "Consultar Relatórios":
    st.subheader("Parâmetros da Consulta")
    col1, col2 = st.columns(2)
    with col1:
        initial_date = st.date_input("Data Inicial")
    with col2:
        end_date = st.date_input("Data Final")
    briefing_id = st.text_input("Briefing ID")
    board_name = st.text_input("Board (opcional)")
    column_name = st.text_input("Coluna (opcional)")

    if st.button("Consultar Relatórios"):
        with st.spinner("Consultando API da Deskfy..."):
            if not st.session_state.api_key or not initial_date or not end_date or not briefing_id:
                st.warning("Preencha todos os campos obrigatórios.")
            else:
                url = "https://service-api.deskfy.io/v1/reports/workflow"
                params = {
                    "initialDate": initial_date.strftime("%Y-%m-%d"),
                    "endDate": end_date.strftime("%Y-%m-%d"),
                    "briefingId": briefing_id
                }
                if board_name:
                    params["boardName"] = board_name
                if column_name:
                    params["columnName"] = column_name

                response = requests.get(url, headers={"x-api-key": st.session_state.api_key}, params=params)

                if response.status_code == 200:
                    data = response.json()
                    if not data:
                        st.info("Nenhum dado encontrado.")
                    else:
                        data_flat = [dict_flatten(item) for item in data]
                        df = pd.DataFrame(data_flat)
                        st.success("Dados obtidos com sucesso.")
                        st.dataframe(df)

                        output_excel = BytesIO()
                        with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
                            df.to_excel(writer, index=False, sheet_name="Relatório")
                            formatar_excel(writer, "Relatório")
                        output_excel.seek(0)

                        st.download_button("Baixar Excel", data=output_excel, file_name="relatorio_deskfy.xlsx")
                        output_csv = df.to_csv(index=False).encode("utf-8")
                        st.download_button("Baixar CSV", data=output_csv, file_name="relatorio_deskfy.csv")
                else:
                    st.error(f"Erro {response.status_code}: {response.text}")

if opcao == "Consultar Detalhes da Solicitação":
    st.subheader("Consultar Detalhes da Solicitação")
    task_id = st.text_input("Digite o Task ID da Solicitação")

    if st.button("Consultar Detalhes"):
        if not task_id:
            st.warning("Por favor, insira um Task ID.")
        else:
            with st.spinner("Consultando API Deskfy..."):
                url = "https://service-api.deskfy.io/v1/reports/workflow/task-details"
                headers = {"x-api-key": st.session_state.api_key}
                params = {"taskId": task_id}
                response = requests.get(url, headers=headers, params=params)

                if response.status_code == 200:
                    data = response.json()
                    linha = {}
                    for key, value in data.items():
                        if isinstance(value, dict):
                            linha.update(dict_flatten(value, prefix=f"{key}."))
                        elif isinstance(value, list):
                            linha[key] = "; ".join(json.dumps(i, ensure_ascii=False) if isinstance(i, dict) else str(i) for i in value)
                        else:
                            linha[key] = value if value is not None else ""

                    if "solicitacao.id" in linha:
                        linha["link_deskfy"] = f"https://app.deskfy.io/task/{linha['solicitacao.id']}"

                    exibir_tabela_formatada(linha)

                    df = pd.DataFrame([linha])
                    output = BytesIO()
                    with pd.ExcelWriter(output, engine="openpyxl") as writer:
                        df.to_excel(writer, index=False, sheet_name="Detalhes")
                        formatar_excel(writer, "Detalhes")
                    output.seek(0)

                    st.download_button(
                        label="📅 Baixar Excel",
                        data=output,
                        file_name=f"detalhes_{linha.get('solicitacao.codigo', task_id)}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                else:
                    st.error(f"Erro {response.status_code}: {response.text}")