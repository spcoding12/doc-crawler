"""
Doc Crawler 入口模块

请直接运行根目录的 main.py:
    python main.py
"""

# 重新导出主入口
import sys
from pathlib import Path

# 添加根目录到路径
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from main import main

if __name__ == "__main__":
    main()
