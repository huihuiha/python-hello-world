#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Hello World 测试模块
单元测试和功能测试
"""

import unittest
from hello import main


class TestHelloWorld(unittest.TestCase):
    """Hello World 程序的测试用例"""

    def test_main_exists(self):
        """测试 main 函数是否存在"""
        self.assertTrue(callable(main), "main 函数应该存在")

    def test_output_hello_world(self):
        """测试输出 'Hello, World!'"""
        from io import StringIO
        import sys

        # 捕获输出
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__

        # 验证输出
        output = captured_output.getvalue()
        self.assertIn("Hello, World!", output)

    def test_output_chinese(self):
        """测试输出中文欢迎信息"""
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("欢迎来到 Python 编程世界", output)

    def test_function_callable(self):
        """测试 main 函数可以正常调用"""
        try:
            main()
            # 如果能正常调用，说明函数没有语法错误
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"main 函数调用失败: {e}")


class TestHelloWorldFeatures(unittest.TestCase):
    """测试 Hello World 的功能特性"""

    def test_no_arguments_required(self):
        """测试不需要任何参数"""
        try:
            main()
        except TypeError as e:
            self.fail(f"main 函数不应该需要参数: {e}")

    def test_print_statements(self):
        """测试程序会打印信息"""
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertGreater(len(output), 0, "应该有输出内容")


if __name__ == "__main__":
    # 运行测试
    unittest.main(verbosity=2)
