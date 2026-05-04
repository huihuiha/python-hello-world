# Python Hello World 项目

一个简单的 Python Hello World 程序示例，包含基础版本、增强版本和完整测试。

## 项目说明

这是一个入门级的 Python 项目，演示基本的 Python 程序结构、功能扩展和测试方法。

## 代码结构

```
python-hello-world/
├── hello.py           # 基础版本
├── hello_v2.py        # 增强版本（命令行参数、颜色输出）
├── test_hello.py      # 单元测试（unittest框架）
├── test_sample.py     # 功能测试示例
├── tests/
│   └── README.md       # 测试文档
├── .gitignore
├── requirements.txt    # 依赖列表（pytest等）
└── README.md          # 本文件
```

## 功能特点

### 基础版本 (hello.py)
- ✅ 简单的函数调用
- ✅ 使用 `if __name__ == "__main__"` 模式
- ✅ 中文注释和输出支持
- ✅ emoji 支持

### 增强版本 (hello_v2.py)
- ✅ 命令行参数支持（argparse）
- ✅ 彩色输出（ANSI 颜色代码）
- ✅ 个性化问候（-n/--name 参数）
- ✅ 系统信息显示（-i/--info 参数）
- ✅ 颜色选择（-c/--color 参数）
- ✅ 时间感知问候（早上/下午/晚上）

## 运行方法

### 基础版本
```bash
python3 hello.py
```

### 增强版本
```bash
# 基本运行
python3 hello_v2.py

# 个性化问候
python3 hello_v2.py -n "林总"

# 显示系统信息
python3 hello_v2.py -i

# 指定输出颜色
python3 hello_v2.py -c green

# 显示帮助信息
python3 hello_v2.py --help
```

## 测试

### 运行单元测试
```bash
# 安装测试依赖
pip install -r requirements.txt

# 运行所有单元测试
python3 test_hello.py -v

# 运行特定测试
python3 -m unittest test_hello.TestHelloWorld.test_main_exists
```

### 运行功能测试
```bash
python3 test_sample.py
```

## 测试内容

### test_hello.py（单元测试）
- ✅ main 函数存在性测试
- ✅ "Hello, World!" 输出验证
- ✅ 中文欢迎信息输出测试
- ✅ 函数可调用性测试
- ✅ 无参数要求测试
- ✅ 输出内容测试

### test_sample.py（功能测试）
- ✅ 基本功能测试
- ✅ 模块导入测试
- ✅ 函数可调用性测试
- ✅ 执行时间测试

## 依赖安装

```bash
# 安装测试依赖
pip install -r requirements.txt
```

**主要依赖：**
- pytest==8.2.0 - 单元测试框架
- pytest-cov==4.1.0 - 测试覆盖率

**可选依赖：**
- black==24.4.2 - 代码格式化
- pylint==3.1.0 - 代码检查

## 输出结果

### 基础版本
```
Hello, World!
欢迎来到 Python 编程世界！🐍
```

### 增强版本
```
╔═══════════════════════════════════╗
║   Python Hello World v2 - 增强版本       ║
╚═══════════════════════════════════╝
早上好, 林总！
现在是 23:40，很高兴见到你！

✨ 代码学习之旅开始！
```

### 系统信息输出
```
📊 系统信息：
  Python 版本: 3.12.0
  当前时间: 2026-05-04 23:40:12
  平台: linux
```

## 开发建议

1. ✅ 添加更多单元测试到 `test_hello.py`
2. ✅ 添加集成测试
3. ✅ 配置 CI/CD（GitHub Actions）
4. ✅ 添加代码覆盖率报告
5. ✅ 添加更多命令行参数
6. ✅ 实现文件读写功能
7. ✅ 添加错误处理和异常捕获

## 许可证

MIT License
