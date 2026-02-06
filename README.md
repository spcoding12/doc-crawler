# Doc Crawler

通用技术文档爬取工具 - 将任意技术文档网站批量抓取并保存到本地。

## 功能特性

- 🔍 自动识别文档框架（Docusaurus、VuePress、MkDocs、GitBook）
- 📄 多种输出格式（单MD、多MD、JSON）
- 🖼️ 自动下载图片
- 🎯 交互式操作

## 安装

```bash
pip install -r requirements.txt
```

## 使用

```bash
python -m src.main
```

按提示输入文档URL即可。

## 文档

- [需求规格](docs/requirements_v1.md)
- [实现方案](docs/implementation_plan.md)
