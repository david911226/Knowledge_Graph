import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network
import logic

# 呼叫邏輯層的初始化
logic.initialize_session_state()

# 設定頁面標題
st.title("互動式故事知識圖譜建構工具")

# 側邊欄 UI 設計
with st.sidebar:
    st.header("控制面板")

    # 新增角色區塊
    with st.expander("新增角色"):
        char_name = st.text_input("角色名稱", key="char_name")
        char_desc = st.text_area("角色描述", key="char_desc")
        if st.button("確認新增角色"):
            logic.add_character(char_name, char_desc)

    # 新增關係區塊
    with st.expander("新增關係"):
        # 獲取已存在的角色列表作為選項
        existing_chars = list(st.session_state['graph'].nodes)
        
        source_char = st.selectbox("來源角色", options=existing_chars, key="source_char")
        target_char = st.selectbox("目標角色", options=existing_chars, key="target_char")
        rel_type = st.text_input("關係類型 (例如:朋友、敵人)", key="rel_type")
        
        if st.button("確認新增關係"):
            if source_char != target_char:
                logic.add_relationship(source_char, target_char, rel_type)
            else:
                st.error("來源和目標角色不能相同！")

    # 專案管理區塊
    st.header("專案管理")
    project_name = st.text_input("專案檔名", value="my_story")
    if st.button("儲存圖譜"):
        logic.save_graph_to_json(project_name)

    uploaded_file = st.file_uploader("載入圖譜 JSON", type="json")
    if uploaded_file is not None:
        logic.load_graph_from_json(uploaded_file)
        st.rerun()

# 視覺化圖譜函式
def draw_graph():
    """將 NetworkX 圖譜轉換為 pyvis HTML 並顯示"""
    if not st.session_state['graph'].nodes:
        st.warning("目前圖譜中沒有任何角色，請先新增。")
        return

    # 初始化 pyvis Network
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=True, directed=True)
    
    # 從 NetworkX graph 添加節點和邊
    net.from_nx(st.session_state['graph'])

    # 讓 PyVis 使用「有向圖」的預設排版，避免雙向關係線條重疊
    net.set_options("""
    var options = {
      "edges": {
        "arrows": {
          "to": {
            "enabled": true,
            "scaleFactor": 1
          }
        },
        "smooth": {
          "type": "curvedCW",
          "roundness": 0.2
        }
      }
    }
    """)
    
    # 產生 HTML 檔案
    try:
        net.save_graph("graph.html")
        
        # 在 Streamlit 中讀取並顯示 HTML
        with open("graph.html", "r", encoding="utf-8") as f:
            html_data = f.read()
        components.html(html_data, height=800)
    except Exception as e:
        st.error(f"視覺化產生失敗: {e}")

# 主介面顯示
st.write("### 角色關係網絡圖")
draw_graph()