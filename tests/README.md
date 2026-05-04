# 测试文档

## 测试文件说明

本项目包含两个测试文件：

### 1. test_hello.py
**单元测试框架：** unittest

**测试内容：**
- ✅ main 函数存在性测试
- ✅ "Hello, World!" 输出测试
- ✅ 中文欢迎信息输出测试
- ✅ 函数可调用性测试
- ✅ 无参数要求测试
- ✅ 输出内容测试

**运行方式：**
```bash
# 运行所有测试
python3 test_hello.py

# 运行特定测试
python3 -m unittest test_hello.TestHelloWorld.test_main_exists

# 详细输出
python3 -m unittest -v test_hello
```

### 2. test_sample.py
**功能测试框架：** 自定义

**测试内容：**
- ✅ 基本功能测试
- ✅ 模块导入测试
- ✅ 函数可调用性测试
- ✅ 执行时间测试

**运行方式：**
```bash
python3 test_sample.py
```

## 测试覆盖率

**被测试的模块：**
- `hello.py` - 主程序模块
- `hello_v2.py` - 增强版本模块

**测试类型：**
- 单元测试
- 功能测试
- 性能测试（执行时间）

## 新增功能测试

### 命令行参数测试
```python
# 测试 -n/--name 参数
python3 hello_v2.py -n "林总"

# 测试 -i/--info 参数
python3 hello_v2.py -i

# 测试 -c/--color 参数
python3 hello_v2.py -c green
```

### 颜色输出测试
验证不同颜色参数的输出效果：
- red, green, yellow, blue, cyan, magenta

### 系统信息测试
验证系统信息的正确性：
- Python 版本
- 当前时间
- 平台信息

## 运行所有测试

```bash
# 运行单元测试
python3 test_hello.py -v

# 运行功能测试
python3 test_sample.py
```

## 测试结果预期

所有测试应该通过，没有错误或失败。

如果测试失败，检查：
1. Python 版本是否 >= 3.6
2. 文件路径是否正确
3. 导入路径是否正确
