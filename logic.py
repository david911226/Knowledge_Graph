import streamlit as st
import networkx as nx
import json

# 初始化與狀態管理
def initialize_session_state():
    """初始化 Session State，確保圖譜物件存在"""
    if 'graph' not in st.session_state:
        # 創建一個空的 NetworkX 圖物件
        st.session_state['graph'] = nx.DiGraph()

# 核心邏輯函式
def add_character(name, description=""):
    """新增一個角色節點到圖中"""
    if name and not st.session_state['graph'].has_node(name):
        st.session_state['graph'].add_node(name, title=description, type='character')
        st.success(f"角色 '{name}' 新增成功！")
    elif name:
        st.warning(f"角色 '{name}' 已存在。")

def add_relationship(source, target, relationship_type):
    """新增一條關係邊到圖中"""
    # 檢查是否已經有 "source -> target" 的關係
    if st.session_state['graph'].has_edge(source, target):
        st.warning(f"'{source}' 到 '{target}' 的關係已存在。")
    else:
        # DiGraph 會自動記錄方向
        st.session_state['graph'].add_edge(source, target, label=relationship_type)
        st.success(f"成功建立關係：{source} --[{relationship_type}]--> {target}")

# 資料持久化
def save_graph_to_json(filename):
    """將圖譜資料儲存為 JSON 檔案"""
    try:
        graph_data = nx.node_link_data(st.session_state['graph'])
        # 確保 data 資料夾已存在
        with open(f"data/{filename}.json", "w", encoding="utf-8") as f:
            json.dump(graph_data, f, ensure_ascii=False, indent=4)
        st.success(f"圖譜已成功儲存至 data/{filename}.json")
    except Exception as e:
        st.error(f"儲存失敗：{e}")

def load_graph_from_json(uploaded_file):
    """從上傳的 JSON 檔案讀取圖譜資料"""
    try:
        graph_data = json.load(uploaded_file)
        st.session_state['graph'] = nx.node_link_graph(graph_data, directed=True)
        st.success(f"已成功從 {uploaded_file.name} 載入圖譜！")
    except Exception as e:
        st.error(f"載入失敗：{e}")