#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello World 程序示例用法和测试
展示如何调用和测试 hello.py
"""

from hello import main


def test_basic_functionality():
    """测试基本功能"""
    print("=== 测试 1: 基本功能测试 ===")
    print("正在调用 main() 函数...")
    main()
    print("✅ 基本功能测试通过！")


def test_module_import():
    """测试模块导入"""
    print("\n=== 测试 2: 模块导入测试 ===")
    print("正在导入 hello 模块...")
    from hello import main
    print(f"✅ 模块导入成功！main 函数: {main}")


def test_function_callable():
    """测试函数可调用性"""
    print("\n=== 测试 3: 函数可调用性测试 ===")
    print("正在测试 main 函数是否可调用...")
    if callable(main):
        print("✅ main 函数可调用！")
    else:
        print("❌ main 函数不可调用！")


def test_execution_time():
    """测试执行时间"""
    import time

    print("\n=== 测试 4: 执行时间测试 ===")
    print("正在测量执行时间...")
    start_time = time.time()
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"✅ 执行时间: {execution_time:.6f} 秒")


def run_all_tests():
    """运行所有测试"""
    print("🧪 开始运行 Hello World 程序测试套件\n")
    print("=" * 50)

    try:
        test_basic_functionality()
        test_module_import()
        test_function_callable()
        test_execution_time()

        print("\n" + "=" * 50)
        print("🎉 所有测试完成！")

    except Exception as e:
        print(f"\n❌ 测试过程中出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_all_tests()
