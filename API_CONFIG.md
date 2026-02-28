# API 配置摘要

**最后更新:** 2026-02-24

## 已配置的 API 提供商

### 主要模型提供商

| 提供商 | 状态 | 模型 | 备注 |
|--------|------|------|------|
| LongCat | ✅ | LongCat-Flash-Lite, LongCat-Flash-Thinking-2601 | 2 个 Key 轮询，1 亿 Token/日 |
| NVIDIA NIM | ✅ | Kimi K2.5, GLM-5, Qwen3.5 397B | 2 个 Key 轮询 |
| OpenCode | ✅ | Kimi K2.5 Free, GLM-5 Free, Minimax M2.5 Free, Big Pickle, Trinity Large | 4 个 Key 轮询 |
| iFlow | ✅ | Qwen3 Max | 默认模型 |
| Antigravity | ✅ | Gemini 3.1 Pro High | Fallback |

### 其他服务

| 服务 | 状态 | 用途 |
|------|------|------|
| Telegram Bot | ✅ | 消息推送 |
| GitHub Copilot | ✅ | 代码补全 |
| Google | ✅ | 多模态任务 |
| OpenRouter | ✅ | Fallback |
| Qianfan (百度) | ✅ | 中文模型任务 |
| Mistral | ✅ | 欧洲模型任务 |

## Cron 任务配置

| 任务 ID | 频率 | 模型 | 说明 |
|--------|------|------|------|
| lite-mega-learning | 每 4 小时 | LongCat-Flash-Lite | 大规模学习 (1 亿 Token/日) |
| tech-news-hourly | 每小时 | LongCat-Flash-Thinking-2601 | 科技新闻更新 |
| social-media-trends | 每日 4 次 | LongCat-Flash-Thinking-2601 | 社群趋势观察 |
| daily-summary-report | 每日 23:30 | LongCat-Flash-Thinking-2601 | 学习总结报告 |
| weekly-memory-cleanup | 每周日 10:00 | LongCat-Flash-Thinking-2601 | 记忆清理 |

## 默认模型配置

- **主要模型**: `iflow/qwen3-max`
- **Fallback 链**: 
  1. antigravity/gemini-3.1-pro-high
  2. longcat-2601-1/LongCat-Flash-Thinking-2601
  3. longcat-2601-2/LongCat-Flash-Thinking-2601
  4. nvidia-nim-1/moonshotai/kimi-k2.5
  5. opencode-1/glm-5-free

## 注意事项

- 所有 API Key 都存储在 `openclaw.json` 和 `auth-profiles.json` 中
- 不要将这些文件提交到公共仓库
- API Key 轮询机制确保高可用性
- 速率限制错误会自动触发 fallback
