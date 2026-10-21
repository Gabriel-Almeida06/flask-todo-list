import streamlit as st
import requests


API_URL = "http://127.0.0.1:5001/tarefas"


st.set_page_config(page_title="Gerenciador de Tarefas", page_icon="📝", layout="centered")

st.title("📝 Gerenciador de Tarefas")
st.write("Interface em Python desenvolvida com **Streamlit** conectada à API Flask.")

st.divider()

# --- FORMULÁRIO PARA CRIAR TAREFA (POST) ---
st.subheader("➕ Nova Tarefa")

with st.form(key="form_nova_tarefa", clear_on_submit=True):
    titulo = st.text_input("Título da tarefa*", placeholder="Ex: Estudar Streamlit")
    descricao = st.text_area("Descrição", placeholder="Ex: Aprender a integrar com API Flask")
    submit_button = st.form_submit_button(label="Adicionar Tarefa")

if submit_button:
    if not titulo.strip():
        st.warning("O título é obrigatório!")
    else:
        # Envia requisição POST para a API Flask
        payload = {"titulo": titulo, "descricao": descricao}
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 201:
            st.success("Tarefa criada com sucesso!")
            st.rerun()  # Recarrega a página para atualizar a lista
        else:
            st.error("Erro ao criar tarefa.")

st.divider()

# --- LISTAGEM E AÇÕES (GET, PUT, DELETE) ---
st.subheader("📋 Suas Tarefas")

try:
    # Busca todas as tarefas via GET
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        tarefas = response.json()

        if not tarefas:
            st.info("Nenhuma tarefa cadastrada no momento.")
        else:
            for tarefa in tarefas:
                col1, col2, col3 = st.columns([0.6, 0.2, 0.2])

                # Coluna 1: Título e Descrição
                with col1:
                    status_icon = "✅" if tarefa["concluida"] else "⏳"
                    st.markdown(f"**{status_icon} {tarefa['titulo']}**")
                    if tarefa.get("descricao"):
                        st.caption(tarefa["descricao"])

                # Coluna 2: Alternar Concluída (PUT)
                with col2:
                    novo_status = not tarefa["concluida"]
                    btn_label = "Refazer" if tarefa["concluida"] else "Concluir"
                    if st.button(btn_label, key=f"status_{tarefa['id']}"):
                        requests.put(f"{API_URL}/{tarefa['id']}", json={"concluida": novo_status})
                        st.rerun()

                # Coluna 3: Excluir Tarefa (DELETE)
                with col3:
                    if st.button("🗑️ Excluir", key=f"del_{tarefa['id']}"):
                        requests.delete(f"{API_URL}/{tarefa['id']}")
                        st.rerun()

                st.markdown("---")
    else:
        st.error("Não foi possível carregar as tarefas da API.")

except requests.exceptions.ConnectionError:
    st.error("⚠️ Não foi possível conectar à API Flask. Verifique se o servidor `app.py` está rodando na porta 5001!")