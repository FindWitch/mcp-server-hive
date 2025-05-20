import os
import logging
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from pyhive import hive

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 加载环境变量
load_dotenv()

# 初始化 MCP 服务器
mcp = FastMCP("HiveServer")

def get_hive_connection():
    """获取 Hive 连接"""
    try:
        host = os.getenv("HIVE_HOST", "10.50.71.14")
        port = int(os.getenv("HIVE_PORT", "10000"))
        username = os.getenv("HIVE_USERNAME", "qiannan")
        password = os.getenv("HIVE_PASSWORD", "nan-qian@dd-lab")
        
        logger.info(f"正在连接到 Hive 服务器: {host}:{port}")
        
        return hive.Connection(
            host=host,
            port=port,
            username=username,
            password=password
        )
    except Exception as e:
        logger.error(f"连接 Hive 服务器失败: {str(e)}")
        raise

@mcp.tool()
async def execute_query(query: str) -> str:
    """
    执行 Hive SQL 查询
    
    参数:
        query (str): SQL 查询语句
        
    返回:
        str: 查询结果
    """
    try:
        conn = get_hive_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        
        # 获取列名
        columns = [desc[0] for desc in cursor.description]
        
        # 获取数据
        results = cursor.fetchall()
        
        # 格式化结果
        formatted_results = []
        for row in results:
            formatted_results.append(dict(zip(columns, row)))
            
        cursor.close()
        conn.close()
        
        return f"✅ 查询成功:\n{formatted_results}"
    except Exception as e:
        return f"❌ 查询失败: {str(e)}"

@mcp.tool()
async def list_tables() -> str:
    """
    列出当前数据库中的所有表
    
    返回:
        str: 表列表
    """
    try:
        conn = get_hive_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return f"✅ 当前数据库中的表:\n{[table[0] for table in tables]}"
    except Exception as e:
        return f"❌ 获取表列表失败: {str(e)}"

@mcp.tool()
async def describe_table(table_name: str) -> str:
    """
    获取表的详细信息
    
    参数:
        table_name (str): 表名
        
    返回:
        str: 表结构信息
    """
    try:
        conn = get_hive_connection()
        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return f"✅ 表 {table_name} 的结构:\n{columns}"
    except Exception as e:
        return f"❌ 获取表结构失败: {str(e)}"

if __name__ == "__main__":
    try:
        logger.info("正在启动 MCP 服务器...")
        mcp.run(transport='stdio')
    except Exception as e:
        logger.error(f"MCP 服务器启动失败: {str(e)}")
        raise 