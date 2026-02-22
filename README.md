# AI 每日學習倉庫

自動使用 AI 模型學習最新 AI 資訊並保存報告。

## 功能

- 🤖 使用 LongCat-Flash-Thinking-2601 模型
- 📰 自動收集 AI 領域新聞和進展
- 📊 生成結構化學習報告
- ☁️ 自動同步到 GitHub 儲存

## 報告位置

所有報告保存在 `ai-reports/` 目錄中，格式：`AI 學習日報_YYYY-MM-DD.md`

## 自動執行

每天 08:00 自動執行學習和同步。

## 手動執行

```bash
# 執行學習
python AI 每日自動學習.py

# 僅同步到 GitHub
python sync_to_github.py

# 同步所有歷史報告
python sync_to_github.py --all
```

## 使用模型

- **主要**: LongCat-Flash-Thinking-2601 (1000 萬 tokens/天)
- **Fallback**: Qwen3 Max, DeepSeek R1

---

由 OpenClaw 自動驅動
