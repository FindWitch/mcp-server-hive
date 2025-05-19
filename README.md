# MCP Hive Server

## 项目简介

本项目基于 MCP 框架，实现了一个用于操作 Hive 数据库的服务端。通过 MCP 工具接口，可以远程执行 Hive SQL 查询、列出数据库表、查看表结构等操作，适用于数据分析、自动化运维等场景。

## 目录结构

```
.
├── hive_server.py      # MCP Hive 服务主程序
├── pyproject.toml      # Python 项目依赖与元数据
├── .python-version     # Python 版本要求
├── README.md           # 项目说明文档
```

## 环境要求

- Python 3.12 及以上
- Hive 数据库可访问
- 推荐使用虚拟环境（如 .venv）

## 依赖安装

本项目依赖已在 `pyproject.toml` 中声明，主要包括：
- python-dotenv
- mcp
- openai
- pyhive

### 安装步骤

1. 创建虚拟环境（可选）：
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. 安装依赖：
```bash
pip install -e .  # 使用 pyproject.toml
```

## 环境变量配置

请在项目根目录下创建 `.env` 文件，配置 Hive 连接信息，例如：

```env
HIVE_HOST=127.0.0.1
HIVE_PORT=10000
HIVE_USERNAME=root
HIVE_PASSWORD=your_password
```

## 启动服务

```bash
python hive_server.py
```

日志会输出 Hive 连接和 MCP 服务启动信息。

## MCP 工具接口说明

### 1. 执行查询
- 接口：`execute_query(query: str)`
- 功能：执行 Hive SQL 查询
- 返回：查询结果

### 2. 列出表
- 接口：`list_tables()`
- 功能：列出当前数据库下所有表
- 返回：表名列表

### 3. 查看表结构
- 接口：`describe_table(table_name: str)`
- 功能：查看指定表的结构信息
- 返回：表结构信息






