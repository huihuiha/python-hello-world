#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Hello World v2 - 增强版本
添加了命令行参数、颜色输出和更多交互功能
"""

import argparse
import sys
from datetime import datetime


class Color:
    """ANSI 颜色代码"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


def print_colored(text, color=Color.WHITE):
    """打印带颜色的文本"""
    print(f"{color}{text}{Color.RESET}")


def greet_world():
    """基础的 Hello World 输出"""
    print_colored("Hello, World!", Color.GREEN)
    print_colored("欢迎来到 Python 编程世界！🐍", Color.CYAN)


def greet_name(name):
    """个性化问候 - 根据名字输出问候"""
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "早上好"
    elif 12 <= current_hour < 18:
        greeting = "下午好"
    else:
        greeting = "晚上好"

    print_colored(f"{greeting}, {name}！", Color.YELLOW)
    print_colored(f"现在是 {datetime.now().strftime('%H:%M')}，很高兴见到你！", Color.CYAN)


def show_system_info():
    """显示系统信息"""
    print_colored("\n📊 系统信息：", Color.BLUE)
    print(f"  Python 版本: {sys.version.split()[0]}")
    print(f"  当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  平台: {sys.platform}")


def main():
    """主函数，处理命令行参数和调用相应功能"""
    parser = argparse.ArgumentParser(
        description='Python Hello World v2 - 增强版本',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '-n', '--name',
        type=str,
        help='个性化问候，指定名字'
    )

    parser.add_argument(
        '-i', '--info',
        action='store_true',
        help='显示系统信息'
    )

    parser.add_argument(
        '-c', '--color',
        choices=['red', 'green', 'yellow', 'blue', 'cyan', 'magenta'],
        help='指定输出颜色'
    )

    args = parser.parse_args()

    # 显示欢迎信息
    print_colored("╔═══════════════════════════════════╗", Color.MAGENTA)
    print_colored("║   Python Hello World v2 - 增强版本       ║", Color.MAGENTA)
    print_colored("╚═══════════════════════════════════╝", Color.MAGENTA)

    # 根据参数执行不同功能
    if args.info:
        show_system_info()

    if args.name:
        greet_name(args.name)
    else:
        greet_world()

    print_colored("\n✨ 代码学习之旅开始！", Color.GREEN)


if __name__ == "__main__":
    main()
