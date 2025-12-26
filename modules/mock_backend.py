import networkx as nx
import random

class GraphManager:
    def __init__(self):
        # 這裡之後會換成真的資料庫載入邏輯
        pass

    def get_initial_graph(self):
        """回傳一個測試用的預設圖譜，讓你開發時不至於看到空白畫面"""
        G = nx.Graph()
        # 預設一些哈利波特的數據讓畫面好看
        G.add_node("哈利波特", title="存活下來的男孩", type="character", group=1)
        G.add_node("榮恩", title="哈利的好友", type="character", group=1)
        G.add_node("妙麗", title="萬事通", type="character", group=1)
        G.add_node("鄧不利多", title="校長", type="character", group=2)
        G.add_edge("哈利波特", "榮恩", label="摯友")
        G.add_edge("哈利波特", "妙麗", label="摯友")
        G.add_edge("哈利波特", "鄧不利多", label="師生")
        return G

    def add_character(self, graph, name, description):
        """模擬新增角色"""
        if graph.has_node(name):
            return False, f"⚠️ 角色 '{name}' 已經存在囉！"
        
        # 實際上這行不會真的存檔，因為這是 Mock，但會更新當下的 Graph 物件
        graph.add_node(name, title=description, type="character", group=1)
        return True, f"✅ 成功新增角色：{name}"

    def add_relationship(self, graph, source, target, relation):
        """模擬新增關係"""
        if graph.has_edge(source, target):
            return False, f"⚠️ '{source}' 和 '{target}' 之間已經有關係了。"
        
        graph.add_edge(source, target, label=relation)
        return True, f"🔗 成功連結：{source} --[{relation}]--> {target}"
    
    def save_graph(self, graph, filename):
        """模擬存檔"""
        return True, f"💾 專案 '{filename}' 已儲存 (模擬模式)"