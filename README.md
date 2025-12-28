# 互動式故事知識圖譜建構工具 (Interactive Story Knowledge Graph)

這是一個基於 Python 的互動式工具，旨在協助創作者、讀者或研究人員透過圖形化介面，手動建構並視覺化故事中角色與角色之間的複雜關係網絡。

## 📂 檔案結構說明

本專案採用 **前後端分離 (Separation of Concerns)** 的設計模式，將邏輯運算與使用者介面拆分為兩個核心檔案：

### 1. `logic.py` (後端邏輯層)

- **功能**：
- 負責所有資料結構的處理（使用 `NetworkX`）。
- 管理 Session State 初始化。
- 執行核心運算，如：新增角色節點、建立關係邊、檢查重複資料。
- 處理資料持久化（將圖譜儲存為 `.json` 檔案或讀取）。

- **注意**：此檔案不包含任何 UI 元件的繪製，僅提供函式供介面呼叫。

### 2. `interface.py` (前端介面層)

- **功能**：
- 基於 `Streamlit` 框架建構網頁介面。
- 設計側邊欄、輸入框、按鈕等互動元件。
- 負責接收使用者輸入，並呼叫 `logic.py` 的函式來處理資料。
- 負責視覺化呈現，將圖譜轉換為互動式 HTML (使用 `PyVis`)。

---

## 🚀 快速開始 (Quick Start)

### 1. 環境設定

確保您已安裝 Python 3.8 或以上版本。建議使用虛擬環境 (Virtual Environment) 以避免套件衝突。

```bash
# 建立虛擬環境 (macOS/Linux)
python3 -m venv venv
source venv/bin/activate

# 建立虛擬環境 (Windows)
python -m venv venv
venv\Scripts\activate

```

### 2. 安裝依賴套件

```bash
pip install streamlit networkx pyvis

```

### 3. 啟動程式

由於 `interface.py` 是我們的主介面入口，請使用以下指令啟動應用程式：

```bash
streamlit run interface.py

```

_注意：請勿直接執行 `python interface.py` 或 `python logic.py`，這將無法啟動 Streamlit 伺服器。_

---

## ✨ 功能特色

- **角色管理**：可新增角色名稱與描述。
- **關係定義**：定義角色之間的互動關係（如：朋友、敵人、家人）。
- **即時視覺化**：新增資料後，右側畫布會即時更新網絡圖。
- **專案存取**：支援將目前的圖譜儲存為 JSON 檔，並可隨時載入繼續編輯。

---

## 🛠️ 技術棧

- **語言**: Python

- **介面框架**: Streamlit

- **圖形運算**: NetworkX

- **視覺化**: PyVis
