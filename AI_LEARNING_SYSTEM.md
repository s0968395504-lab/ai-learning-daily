# OpenClaw AI 學習系統配置說明

## 📋 已清理的文件

已刪除以下無用備份文件：
- `openclaw.json.bak`
- `openclaw.json.backup`
- `openclaw.json.bak.*`
- `cron/jobs.json.bak`

## 🤖 AI 學習任務配置

### 定時任務列表

| 頻率 | 任務名稱 | 使用模型 | Token 預算 | 說明 |
|------|----------|----------|------------|------|
| **每小時** | 💻 科技新聞更新 | Minimax M2.5 Free | 500 萬/日 | 監控 Hacker News、GitHub Trending |
| **每 2 小時** | 📰 即時新聞掃描 | GLM-5 Free | 600 萬/日 | 台灣、國際、科技新聞 |
| **每日 4 次** | 📱 社群媒體趨勢 | Big Pickle | 800 萬/日 | Twitter、Reddit、YouTube |
| 08:00 | 🤖 每日 AI 學習 | Kimi K2.5 Free | 2000 萬 | 搜尋最新 AI 技術論文和趨勢 |
| 10:00 | 🐙 GitHub 專案觀察 | GLM-5 Free | 1500 萬 | 分析熱門 AI/ML 專案 |
| 14:00 | 🤗 HuggingFace 模型偵察 | Minimax M2.5 Free | 1500 萬 | 尋找可替代的新型號 |
| 16:00 | 🐙 GitHub 專案觀察 | GLM-5 Free | 1500 萬 | 下午場次 |
| 19:00 | 📁 程式碼結構學習 | Big Pickle | 1500 萬 | 學習本地程式碼架構 |
| 23:30 | 📊 每日學習總結報告 | Trinity Large Preview | 500 萬 | 生成並發送總結報告 |
| 00:00 | 🔥 LongCat 燃燒任務 | Flash Lite | 1 億 | 燃燒多餘 Tokens |
| 週日 10:00 | 🧹 每週記憶清理 | - | - | 清理 7 天前舊檔案 |

### 即時資訊觀察配置

| 任務 | 頻率 | 監控來源 | 輸出檔案 |
|------|------|----------|----------|
| 科技新聞 | 每小時 | Hacker News, GitHub Trending, Product Hunt, AI 公司博客 | `memory/tech-news-YYYY-MM-DD-HH.md` |
| 即時新聞 | 每 2 小時 | 台灣新聞、國際新聞、科技新聞、PTT、Dcard | `memory/news-YYYY-MM-DD-HH.md` |
| 社群趨勢 | 每日 4 次 | Twitter/X Hashtag, Reddit, YouTube | `memory/social-trends-YYYY-MM-DD.md` |

### 每日 Token 預算分配

| 項目 | Token 數量 | 佔比 |
|------|------------|------|
| LongCat Flash Lite 燃燒 | 100,000,000 | 69.0% |
| 每日 AI 學習 | 20,000,000 | 13.8% |
| GitHub 觀察 (2 次) | 30,000,000 | 20.7% |
| HuggingFace 偵察 | 15,000,000 | 10.3% |
| 程式碼結構學習 | 15,000,000 | 10.3% |
| 科技新聞 (24 次/日) | 5,000,000 | 3.4% |
| 即時新聞 (12 次/日) | 6,000,000 | 4.1% |
| 社群趨勢 (4 次/日) | 8,000,000 | 5.5% |
| 總結報告 | 5,000,000 | 3.4% |
| **總計** | **~204,000,000** | **100%** |

## 📁 學習輸出目錄

### Memory 目錄 (`memory/`)
- `ai-learning-YYYY-MM-DD.md` - 每日 AI 學習筆記
- `news-YYYY-MM-DD-HH.md` - 即時新聞掃描記錄（每 2 小時）
- `tech-news-YYYY-MM-DD-HH.md` - 科技新聞更新（每小時）
- `social-trends-YYYY-MM-DD.md` - 社群媒體趨勢（每日 4 次）
- `github-observations.md` - GitHub 專案觀察記錄
- `model-alternatives.md` - HuggingFace 模型替代方案
- `code-structure-analysis.md` - 程式碼結構分析
- `recommended-projects.md` - 推薦的優秀專案

### Logs 目錄 (`logs/`)
- `commands.log` - 所有命令執行日誌
- `token-burn-log.md` - LongCat 燃燒進度記錄
- `gateway-service.log` - Gateway 服務日誌

## 🔧 使用方式

### 啟動 AI 學習系統
```powershell
# 雙擊啟動
start-ai-learning.bat

# 或手動啟動
cd C:\Users\User\.openclaw
.\start-ai-learning.bat
```

### 查看即時資訊
```powershell
# 查看最新新聞
notepad memory\news-%date:~0,4%-%date:~5,2%-%date:~8,2%.md

# 查看最新科技新聞
dir /b memory\tech-news-*.md | sort /R | set /p latest= & notepad memory\%latest%

# 查看今日社群趨勢
notepad memory\social-trends-%date:~0,4%-%date:~5,2%-%date:~8,2%.md

# 查看所有記憶檔案
explorer memory
```

### 手動執行任務
```powershell
# 立即執行新聞掃描
openclaw cron run realtime-news-scan

# 立即執行科技新聞更新
openclaw cron run tech-news-hourly

# 立即執行社群趨勢觀察
openclaw cron run social-media-trends
```

## 🔑 API 配置

### OpenCode (4 個 Key 輪流)
- opencode-1/2/3/4: kimi-k2.5-free, glm-5-free, minimax-m2.5-free, big-pickle, trinity-large-preview

### LongCat
- longcat/flash-lite: 1 億 Token/日燃燒任務

## 📊 監控和統計

### 查看 Cron 任務狀態
```powershell
openclaw cron list
```

### 查看 Token 消耗
```powershell
# 查看今日消耗
type logs\token-burn-log.md

# 查看 Gateway 統計
openclaw gateway stats
```

## ⚙️ 配置修改

如需修改任務配置，編輯：
```
C:\Users\User\.openclaw\cron\jobs.json
```

修改後重啟 Gateway：
```powershell
openclaw gateway restart
```

## 🚨 故障排除

### 任務執行失敗
1. 檢查 Gateway 是否運行：`openclaw gateway status`
2. 查看錯誤日誌：`type logs\gateway-service.log`
3. 重啟 Gateway：`openclaw gateway restart`

### Token 燃燒不足
1. 手動執行燃燒任務：`openclaw cron run longcat-token-burner`
2. 或執行 PowerShell 腳本：`powershell -File burn-longcat-tokens.ps1`

### API Key 限制
如果某個 Key 被限制，系統會自動輪流到下一個 Key。
配置中的 4 個 OpenCode Key 會自動輪流使用。

## 📝 備忘錄

- ✅ 所有任務使用 OpenCode 免費 API，穩定且無需費用
- ✅ LongCat Flash Lite 有 1 億用量/日，專門用於燃燒
- ✅ 學習內容會自動整理到 memory/ 目錄
- ✅ 每日 23:30 自動發送總結報告到 Telegram
- ✅ 即時新聞每 2 小時掃描一次，確保資訊不落後
- ✅ 科技新聞每小時更新，掌握最新技術動態
- ✅ 社群趨勢每日 4 次觀察，了解流行話題

---
配置日期：2026-02-24
最後更新：2026-02-24
