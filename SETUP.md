# GitHub 設置指南

## 步驟 1：創建 GitHub Personal Access Token

1. 前往 https://github.com/settings/tokens
2. 點擊 "Generate new token (classic)"
3. 選擇權限：**repo** (全選)
4. 生成並複製 Token

## 步驟 2：創建 GitHub 倉庫

執行以下命令（替換 YOUR_TOKEN 為你的 Token）：

```powershell
cd C:\Users\User\ai-learning-daily

# 設置遠端
git remote add origin https://YOUR_TOKEN@github.com/s0968395504-lab/ai-learning-daily.git

# 切換分支
git branch -M main

# 推送
git push -u origin main
```

## 步驟 3：如果倉庫不存在

先在 GitHub 上創建空倉庫：
1. 前往 https://github.com/new
2. 倉庫名稱：`ai-learning-daily`
3. 設為 **Private** 或 **Public**
4. 不要初始化 README
5. 創建

然後執行步驟 2 的命令。

## 步驟 4：測試同步

```powershell
cd C:\Users\User\Desktop\主要腳本\AI 聽寫雲端版
python sync_to_github.py
```

## 完成！

現在每天自動學習後會同步到：
https://github.com/s0968395504-lab/ai-learning-daily
