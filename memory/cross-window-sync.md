# 跨窗口上下文同步協議

## 🎯 目標
解決多對話窗口間的上下文同步問題，確保記憶一致性

## 🔍 問題分析
- **窗口A**: 469.3k/200k (上下文爆滿)
- **窗口B**: 47k/200k (當前窗口)
- **記憶不同步**: 重要決策和學習可能丟失

## 🛠 同步策略

### 1. 中央記憶倉庫
- 使用 GitHub 作為中央記憶存儲
- 所有窗口從同一源同步
- 衝突解決機制

### 2. 窗口標識系統
```bash
# 為每個窗口創建唯一標識
python skills/git-notes-memory/memory.py -p $WORKSPACE remember '{"window": "control-ui", "context_usage": "47k/200k"}' -t window-status -i n
```

### 3. 同步觸發條件
- **窗口啟動**: 自動從 GitHub 拉取最新記憶
- **重要決策**: 立即同步到中央倉庫
- **定期同步**: 每30分鐘強制同步
- **上下文過量**: 緊急同步和壓縮

## ⚡ 立即行動方案

### 對於高使用率窗口 (469.3k/200k)
```bash
# 1. 緊急記憶歸檔
python skills/git-notes-memory/memory.py -p $WORKSPACE sync --end '{"summary": "窗口清理", "context_usage": "469k"}'

# 2. 強制 Git 提交
git add .
git commit -m "緊急: 窗口上下文清理 $(date)"

# 3. 推送到 GitHub
git push origin master
```

### 對於當前窗口
```bash
# 1. 拉取最新記憶
python skills/git-notes-memory/memory.py -p $WORKSPACE sync --start

# 2. 記錄同步狀態
python skills/git-notes-memory/memory.py -p $WORKSPACE remember '{"action": "跨窗口同步", "source": "control-ui", "target": "all", "timestamp": "$(date)"}' -t sync -i h
```

## 🔄 自動同步工作流

### HEARTBEAT 集成
在每個窗口的 HEARTBEAT.md 中添加：

```markdown
## 跨窗口同步檢查
- 檢查其他窗口的上下文狀態
- 同步重要記憶到中央倉庫
- 解決記憶衝突
- 報告同步狀態
```

### 同步優先級
1. **Critical 記憶**: 立即同步 (用戶偏好、重要決策)
2. **High 記憶**: 定期同步 (架構選擇、學習經驗)
3. **Normal 記憶**: 批量同步 (一般信息、任務狀態)

## 🛡️ 衝突解決

### 合併策略
- **時間戳優先**: 最新修改覆蓋舊版本
- **重要性優先**: Critical > High > Normal > Low
- **窗口權重**: 主控制窗口優先於其他窗口

### 衝突檢測
```bash
# 檢查記憶衝突
git fetch origin
git merge-base HEAD origin/master

# 解決衝突
python skills/git-notes-memory/memory.py -p $WORKSPACE conflict-resolve
```

## 📊 監控與報告

### 同步狀態面板
- 各窗口上下文使用率
- 記憶同步成功率
- 衝突發生頻率
- 同步延遲時間

### 性能指標
- 跨窗口記憶一致性
- 同步操作耗時
- 衝突解決效率
- 用戶體驗影響