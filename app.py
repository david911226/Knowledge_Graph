# app.py
import streamlit as st
import networkx as nx
import json
from pyvis.network import Network
import streamlit.components.v1 as components

# 1. 初始化 session state
def initialize_session_state():
    if 'graph' not in st.session_state:
        # 創建一個空的 NetworkX 圖物件
        st.session_state['graph'] = nx.Graph()

# 呼叫初始化函式
initialize_session_state()

# 2. 核心邏輯函式
def add_character(name, description=""):
    """新增一個角色節點到圖中"""
    if name and not st.session_state['graph'].has_node(name):
        st.session_state['graph'].add_node(name, title=description, type='character')
        st.success(f"角色 '{name}' 新增成功！")
    elif name:
        st.warning(f"角色 '{name}' 已存在。")

def add_relationship(source, target, relationship_type):
    """新增一條關係邊到圖中"""
    if source and target and relationship_type:
        if st.session_state['graph'].has_edge(source, target):
            # 如果關係已存在，可以選擇更新或提示
            st.warning(f"'{source}' 和 '{target}' 之間的關係已存在。")
        else:
            st.session_state['graph'].add_edge(source, target, label=relationship_type)
            st.success(f"成功建立關係：{source} -[{relationship_type}]-> {target}")

def save_graph_to_json(filename):
    """將圖譜資料儲存為 JSON 檔案"""
    graph_data = nx.node_link_data(st.session_state['graph'])
    with open(f"data/{filename}.json", "w", encoding="utf-8") as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=4)
    st.success(f"圖譜已成功儲存至 data/{filename}.json")

def load_graph_from_json(uploaded_file):
    """從上傳的 JSON 檔案讀取圖譜資料"""
    graph_data = json.load(uploaded_file)
    st.session_state['graph'] = nx.node_link_graph(graph_data)
    st.success(f"已成功從 {uploaded_file.name} 載入圖譜！")

# app.py (在側邊欄 UI 區塊加入)
with st.sidebar:
    # --- 儲存與讀取區塊 ---
    st.header("專案管理")
    project_name = st.text_input("專案檔名", value="my_story")
    if st.button("儲存圖譜"):
        save_graph_to_json(project_name)

    uploaded_file = st.file_uploader("選擇一個圖譜 JSON 檔案來載入", type="json")
    if uploaded_file is not None:
        load_graph_from_json(uploaded_file)
        # 重新整理頁面以顯示載入的圖
        st.rerun()



# 測試 UI 用區塊
#st.divider() # 分隔線
#st.write("後端功能測試區")
#test_name = st.text_input("測試角色名稱")
#if st.button("測試新增角色"):
#    add_character(test_name)
#    # 顯示目前圖裡的節點，證明真的有加進去
#    st.write(st.session_state['graph'].nodes)