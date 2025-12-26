import streamlit as st
import networkx as nx
# 引入我們自製的模組
from modules.mock_backend import GraphManager

# 1. 頁面設定 (必須是第一個 Streamlit 指令)
st.set_page_config(
    page_title="Nexus Graph | 互動式知識圖譜",
    page_icon="🕸️",
    layout="wide", # 使用寬版面，看起來比較專業
    initial_sidebar_state="expanded"
)

# 2. 初始化 Session State (狀態管理)
if 'graph' not in st.session_state:
    # 第一次啟動時，載入我們的假資料
    manager = GraphManager()
    st.session_state['graph'] = manager.get_initial_graph()
    st.session_state['manager'] = manager # 把後端管理器也存起來

# 3. 標題與排版
st.title("🕸️ Nexus Graph 知識圖譜編輯器")
st.markdown("---") # 分隔線

# 4. 側邊欄設計 (目前先放標題，下一步我們填滿它)
with st.sidebar:
    st.header("🎛️ 控制台")
    st.info("目前運作模式：Mocking (模擬數據)")
    st.markdown("---")

# 5. 主畫面分區 (兩欄式佈局：左邊操作，右邊顯示)
col_left, col_right = st.columns([1, 2]) # 左邊寬度 1，右邊寬度 2

with col_left:
    st.subheader("📝 編輯區域")
    st.write("（這裡之後會放入新增角色與關係的表單）")

with col_right:
    st.subheader("📊 圖譜預覽")
    # 暫時先用文字顯示節點數量，證明程式有跑起來
    num_nodes = st.session_state['graph'].number_of_nodes()
    num_edges = st.session_state['graph'].number_of_edges()
    
    # 使用 Metric 元件顯示數據，看起來很專業
    m1, m2 = st.columns(2)
    m1.metric("角色數量", num_nodes)
    m2.metric("關係連結", num_edges)
    
    st.warning("視覺化模組尚未載入 (將在 Step 6 實作)")