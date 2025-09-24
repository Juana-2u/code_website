# 🌐 Website Checker

一个简单的 **网站可用性检测工具**，用 Python 编写。  
输入网址后，脚本会自动补全缺少的 `http://` 协议，并检测网站是否能访问。

---

## 🚀 功能
- 自动补全网址协议（默认 `http://`）。
- 使用 `requests` 检测网站可用性。
- 清晰的可访问 / 不可访问提示。

---

## 📦 环境要求
- Python 3.x
- [requests](https://pypi.org/project/requests/)

---

## 🛠 使用方法

运行脚本：
```
python3 code_website.py
```

---

## 🖥 示例
网站可访问：
```
[+] 可访问: http://example.com
```
网站不可访问：
```
[-] 无法访问: http://nonexistentdomain.test
```
