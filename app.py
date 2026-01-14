import streamlit as st
import networkx as nx
import json
import os
from modules.backend import GraphManager
from modules.visualization import render_interactive_graph
from modules.ui import render_sidebar, render_main_tabs

# 1. 頁面設定
st.set_page_config(
    page_title="Nexus Graph | 互動式知識圖譜",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 初始化 Session State
if 'graph' not in st.session_state:
    manager = GraphManager()
    
    # 嘗試載入範例檔案
    example_file = "data/example_harry_potter.json"
    if os.path.exists(example_file):
        try:
            with open(example_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 創建空圖譜
            graph = nx.DiGraph()
            
            # 載入節點
            for node in data. get('nodes', []):
                graph.add_node(
                    node['id'],
                    label=node.get('label', node['id']),
                    title=node.get('title', '')
                )
            
            # 載入邊
            for edge in data.get('edges', []):
                graph. add_edge(
                    edge['from'],
                    edge['to'],
                    label=edge.get('label', '')
                )
            
            st.session_state['graph'] = graph
            st.session_state['example_loaded'] = True
            
        except Exception as e:
            # 如果載入失敗，使用空圖譜
            st. session_state['graph'] = manager.get_initial_graph()
            st.session_state['example_loaded'] = False
            st.error(f"範例載入失敗：{e}")
    else:
        # 沒有範例檔案，使用空圖譜
        st. session_state['graph'] = manager.get_initial_graph()
        st.session_state['example_loaded'] = False
    
    st.session_state['manager'] = manager
    
    # 清除舊快取
    if 'node_positions' in st.session_state:
        del st.session_state['node_positions']

with open('assets/style.css') as f:
    st.markdown(f'<style>{f. read()}</style>', unsafe_allow_html=True)

# 3. 主標題（改成白色）
st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="color: #FFFFFF; font-size: 2.5em;">
            🕸️ Nexus Graph 知識圖譜編輯器
        </h1>
    </div>
""", unsafe_allow_html=True)

# 顯示範例載入提示（只在第一次顯示）
if st.session_state.get('example_loaded') and 'example_toast_shown' not in st.session_state:
    st.toast("✨ 已載入哈利波特範例圖譜！", icon="📚")
    st.session_state['example_toast_shown'] = True

# 4. 渲染側邊欄
render_sidebar()

# 5. 渲染分頁主功能區
render_main_tabs()

# 6. 渲染圖形
st.divider()
render_interactive_graph(st.session_state['graph'])