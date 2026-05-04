# Python Hello World 项目 - GitHub 创建指南

## 项目结构

```
python-hello-world/
├── .gitignore          # Git 忽略文件配置
├── README.md           # 项目说明文档
├── hello.py           # 主程序文件
├── requirements.txt    # Python 依赖列表
└── PROJECT_SETUP.md  # 本文件
```

## 运行测试

项目已通过运行测试：
```
$ python3 hello.py
Hello, World!
欢迎来到 Python 编程世界！🐍
```

## 创建 GitHub 仓库步骤

### 方法 1：使用 GitHub CLI（推荐）

1. 安装 GitHub CLI（如果未安装）：
```bash
# macOS
brew install gh

# Linux (Ubuntu/Debian)
sudo apt install gh

# 或使用包管理器安装
```

2. 登录 GitHub：
```bash
gh auth login
```

3. 创建仓库：
```bash
gh repo create python-hello-world --public --description "一个简单的 Python Hello World 项目" --source=. --remote=origin
```

4. 推送代码：
```bash
git init
git add .
git commit -m "Initial commit: Python Hello World project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/python-hello-world.git
git push -u origin main
```

### 方法 2：手动创建

1. 在 GitHub 网站创建新仓库
   - 访问：https://github.com/new
   - 仓库名：`python-hello-world`
   - 描述：`一个简单的 Python Hello World 项目`
   - 选择：Public 或 Private
   - 不要初始化 README

2. 初始化 Git 并推送：
```bash
cd /tmp/python-hello-world
git init
git add .
git commit -m "Initial commit: Python Hello World project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/python-hello-world.git
git push -u origin main
```

## 命令示例（替换 YOUR_USERNAME）

```bash
# 初始化 Git
cd /tmp/python-hello-world
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: Python Hello World project"

# 设置远程仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/python-hello-world.git

# 推送到 GitHub
git push -u origin main
```

## 注意事项

1. 将 `YOUR_USERNAME` 替换为你的 GitHub 用户名
2. 确保你有该仓库的创建权限
3. 推送前确认 Git 已正确配置：
```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

## 下一步

创建仓库后，你可以：
- 访问：`https://github.com/YOUR_USERNAME/python-hello-world`
- 添加更多功能到 `hello.py`
- 编写单元测试
- 添加 GitHub Actions 自动化测试

祝你编程愉快！🐍✨
