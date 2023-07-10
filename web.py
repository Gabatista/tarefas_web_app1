import streamlit as st
import funcoes as f

tarefas = f.get_tarefas()

def add_tarefa():
    tarefa = st.session_state["nova_tarefa"] + "\n" #dict que traz o estado da sessão
    tarefas.append(tarefa)
    f.write_tarefas(tarefas)


st.title('Tarefas')
st.subheader('Simples lista de tarefas')
st.write('Acompanhamento de tarefas')


for ind, tarefa in enumerate(tarefas):
    check = st.checkbox(tarefa, key=tarefa)
    if check:
        tarefas.pop(ind)
        f.write_tarefas(tarefas)
        del st.session_state[tarefa]
        st.experimental_rerun()

st.text_input(label="Tarefa",placeholder="Digite uma tarefa",on_change=add_tarefa,key='nova_tarefa')