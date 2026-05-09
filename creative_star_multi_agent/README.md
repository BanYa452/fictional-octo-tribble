
# Creative Star - Multi Agent Content Operating System

一个用于实体店抖音代运营的多 Agent 协同自动化系统。

## 功能
- Strategy Agent：账号定位
- Topic Agent：选题生成
- Script Agent：脚本生成
- Rewrite Agent：文案改写
- Review Agent：质量审核
- Ops Agent：运营回流

## 技术栈
- FastAPI
- Python 3.11
- PostgreSQL
- Redis
- OpenAI / DeepSeek Compatible API

## 启动

```bash
cp .env.example .env
docker compose up --build
```

接口：
POST /workflow/run
