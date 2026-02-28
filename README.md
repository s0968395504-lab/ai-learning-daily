# AI 每日學習倉庫

自動使用 AI 模型學習最新 AI 資訊並保存報告。

## 功能

- 🤖 使用 **LongCat-Flash-Lite** 模型 (1 億 tokens/天)
- 📰 自動收集 AI 領域新聞和進展
- 📊 生成結構化學習報告
- ☁️ 自動同步到 GitHub 儲存
- 🔍 每週監控 GitHub & HuggingFace
- 💡 提供優化建議

## 報告位置

| 報告類型 | 位置 | 頻率 |
|----------|------|------|
| 學習日報 | `ai-reports/AI 學習日報_YYYY-MM-DD.md` | 每天 08:00 |
| 優化週報 | `ai-reports/AI 優化週報_YYYY-Www.md` | 每週一 09:00 |

## 自動執行

| 任務 | 時間 | 腳本 |
|------|------|------|
| 每日學習 | 每天 08:00 | `AI 每日自動學習.py` |
| 優化監控 | 每週一 09:00 | `github_hf_monitor.py` |

## 手動執行

```bash
# 執行每日學習
python AI 每日自動學習.py

# 執行優化監控
python github_hf_monitor.py

# 僅同步到 GitHub
python sync_to_github.py
```

## 使用模型

- **主要**: LongCat-Flash-Lite (1 億 tokens/天)
- **Fallback**: Qwen3 Max, DeepSeek R1, Gemini 2.5 Flash Lite

## 監控範圍

- GitHub Trending AI 項目
- HuggingFace 熱門模型
- AI 工具優化建議

---

由 OpenClaw 自動驅動
