# 通用技术文档爬取工具 - V1 技术实现方案

> **需求规格**：[requirements_v1.md](./requirements_v1.md)  
> **状态**：✅ 方案已确认

---

## 一、技术选型

### 1.1 核心技术栈（混合模式）

| 类别 | 技术 | 说明 |
|------|------|------|
| **语言** | Python 3.10+ | |
| **HTTP请求** | requests | 主要方式，轻量 |
| **浏览器自动化** | Playwright | 可选，仅JS渲染页面需要 |
| **HTML解析** | BeautifulSoup4 | |
| **正文提取** | readability-lxml | 通用算法兜底 |
| **Markdown转换** | html2text | |
| **交互式CLI** | rich + questionary | |

### 1.2 混合模式策略

```
用户输入URL
    ↓
尝试 requests 获取页面
    ↓
检测内容是否完整？
    ├─ 是 → 继续处理
    └─ 否 → 提示用户安装 Playwright
              ├─ 用户同意 → 安装并用 Playwright 重试
              └─ 用户拒绝 → 跳过此网站
```

---

## 二、项目结构

```
doc-crawler/
├── docs/
│   └── requirements_v1.md
├── src/
│   ├── __init__.py
│   ├── main.py              # 交互式入口
│   ├── fetcher.py           # 页面获取（requests/Playwright）
│   ├── detector.py          # 框架检测
│   ├── parser.py            # 侧边栏解析
│   ├── extractor.py         # 内容提取
│   ├── exporter.py          # 输出生成
│   ├── frameworks/          # 框架适配器
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── docusaurus.py
│   │   ├── vuepress.py
│   │   ├── mkdocs.py
│   │   └── gitbook.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── output/
├── tests/
├── requirements.txt
└── README.md
```

---

## 三、任务拆分

> 每个任务可独立实现和验证

### Task 1: 项目初始化
**输入**：无  
**输出**：项目骨架 + requirements.txt  
**验证**：`pip install -r requirements.txt` 成功

---

### Task 2: 页面获取模块 (fetcher.py)
**输入**：URL  
**输出**：HTML字符串  
**功能**：
- `fetch_with_requests(url)` — 用requests获取
- `is_js_rendered(html)` — 检测是否需要JS渲染
- `fetch_with_playwright(url)` — 用Playwright获取（可选）

**验证**：
```python
html = fetch_with_requests("https://fastapi.tiangolo.com/")
assert len(html) > 1000
assert is_js_rendered(html) == False
```

---

### Task 3: 框架检测模块 (detector.py)
**输入**：HTML字符串  
**输出**：框架名称（docusaurus/vuepress/mkdocs/gitbook/unknown）  
**验证**：
```python
html = fetch("https://react.dev/learn")
assert detect_framework(html) == "docusaurus"
```

---

### Task 4: 框架适配器 - 基类 + Docusaurus
**输入**：HTML + BeautifulSoup  
**输出**：侧边栏链接列表 + 内容选择器  
**验证**：用Docker文档测试侧边栏解析

---

### Task 5: 框架适配器 - VuePress/MkDocs/GitBook
**输入**：同上  
**输出**：同上  
**验证**：分别用Vue/FastAPI/某GitBook站点测试

---

### Task 6: 内容提取模块 (extractor.py)
**输入**：HTML + 框架适配器  
**输出**：标题 + Markdown正文 + 图片URL列表  
**功能**：
- 使用适配器的选择器提取内容
- 回退到readability算法
- HTML转Markdown
- 提取图片URL

**验证**：提取单个页面内容，检查Markdown格式

---

### Task 7: 图片下载模块
**输入**：图片URL列表 + 输出目录  
**输出**：本地图片文件 + 更新后的Markdown（本地路径）  
**验证**：下载图片并验证文件存在

---

### Task 8: 输出生成模块 (exporter.py)
**输入**：页面内容列表 + 输出格式 + 目录结构  
**输出**：
- 单MD文件：all.md
- 多MD文件：带序号的目录结构
- JSON文件：pages.json
- 目录索引：index.md

**验证**：生成三种格式并检查结构

---

### Task 9: 交互式入口 (main.py)
**输入**：用户交互  
**输出**：完整爬取流程  
**功能**：
- URL输入
- 框架检测反馈
- 页面发现确认
- 格式选择
- 图片选项
- 进度显示
- 错误报告

**验证**：完整流程测试

---

## 四、实现顺序

```
Task1 → Task2 → Task3 → Task4 → Task5 → Task6 → Task7 → Task8 → Task9
```

---

## 五、验收测试

| 测试站点 | 框架 | 输出格式 |
|---------|------|---------|
| docs.docker.com/get-started/ | Docusaurus | 单MD |
| vuejs.org/guide/ | VuePress | 多MD |
| fastapi.tiangolo.com/tutorial/ | MkDocs | JSON |

---

## 六、已确认事项 ✅

| 事项 | 决策 |
|------|------|
| Python版本 | 3.10+ |
| 配置文件 | 不需要 |
| 爬取模式 | 混合模式（requests为主，Playwright可选） |
