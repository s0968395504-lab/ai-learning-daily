# GitHub 記憶同步配置

## 🎯 目標
將所有記憶功能自動同步到 GitHub，實現跨設備持久化存儲

## 🔧 核心組件

### 1. Git-Notes 記憶系統
- **技能**: `git-notes-memory`
- **功能**: 基於 Git notes 的知識圖譜記憶
- **特點**: 分支感知、版本控制、自動同步

### 2. GitHub 助手
- **技能**: `openclaw-github-assistant`
- **功能**: GitHub 倉庫管理、CI/CD 狀態檢查
- **特點**: 自動化 GitHub 操作

### 3. 記憶同步協議
- **自動同步**: 每次會話開始/結束時同步
- **增量更新**: 只同步新增和修改的記憶
- **衝突解決**: 基於時間戳的合併策略

## ⚙️ 配置設置

### GitHub 倉庫設置
```bash
# 創建專門的記憶倉庫
git init memory-repo
git remote add origin https://github.com/s0968395504-lab/openclaw-memory.git
```

### 環境變數
```bash
# 在 .env 文件中設置
export GITHUB_TOKEN=gho_************************************
export GITHUB_USERNAME=s0968395504-lab
export MEMORY_REPO_URL=https://github.com/s0968395504-lab/openclaw-memory.git
```

## 🔄 同步工作流

### 會話開始時
```bash
# 自動從 GitHub 拉取最新記憶
python3 skills/git-notes-memory/memory.py -p $WORKSPACE sync --start

# 檢查記憶同步狀態
gh repo view s0968395504-lab/openclaw-memory
```

### 會話過程中
```bash
# 自動記錄重要決策和學習
python3 skills/git-notes-memory/memory.py -p $WORKSPACE remember '{"decision": "使用PostgreSQL", "reason": "性能需求"}' -t database -i h

# 自動記錄用戶偏好
python3 skills/git-notes-memory/memory.py -p $WORKSPACE remember '{"preference": "使用tabs而非spaces", "context": "代碼風格"}' -t coding-style -i c
```

### 會話結束時
```bash
# 自動同步到 GitHub
python3 skills/git-notes-memory/memory.py -p $WORKSPACE sync --end '{"summary": "會話總結"}'

# 提交並推送到 GitHub
git add .
git commit -m "記憶更新: $(date)"
git push origin main
```

## 📊 記憶分類

### 重要性等級
- **Critical (c)**: 用戶明確要求記住的偏好和決策
- **High (h)**: 架構決策、重要學習、用戶糾正
- **Normal (n)**: 一般信息、任務狀態、進度更新
- **Low (l)**: 臨時筆記、可能被清理的內容

### 標籤系統
- `decision` - 重要決策
- `preference` - 用戶偏好
- `learning` - 學習經驗
- `task` - 任務狀態
- `context` - 項目上下文
- `bug` - 問題和解決方案

## 🛡️ 安全與隱私

### 加密存儲
- 敏感信息在存儲前加密
- 只有當前會話能解密相關內容
- GitHub 上存儲加密後的數據

### 訪問控制
- 私有 GitHub 倉庫
- 僅限授權設備訪問
- 定期審計訪問日誌

## 🔍 檢索與查詢

### 記憶查詢
```bash
# 搜索特定主題
python3 skills/git-notes-memory/memory.py -p $WORKSPACE search "數據庫選擇"

# 獲取完整記憶詳情
python3 skills/git-notes-memory/memory.py -p $WORKSPACE recall -i <memory_id>

# 獲取主題相關記憶
python3 skills/git-notes-memory/memory.py -p $WORKSPACE get database
```

### GitHub 集成查詢
```bash
# 查看記憶倉庫狀態
gh repo view s0968395504-lab/openclaw-memory

# 檢查同步歷史
git log --oneline -10

# 查看特定文件的變更歷史
git log -p -- memory/
```

## 🚀 自動化集成

### HEARTBEAT 集成
在 HEARTBEAT.md 中添加記憶同步檢查：

```markdown
## 記憶同步檢查
- 檢查記憶同步狀態
- 確保 GitHub 連接正常
- 備份重要記憶到雲端
- 清理過時記憶內容
```

### 錯誤處理
- 網絡中斷時本地緩存記憶
- 恢復連接後自動重試同步
- 衝突檢測和自動合併

## 📈 監控與報告

### 同步狀態
- 最後同步時間
- 同步成功率
- 記憶數量統計
- 存儲空間使用

### 性能指標
- 同步耗時
- 檢索響應時間
- 記憶準確率
- 用戶滿意度