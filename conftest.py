
import sys
import os
import pytest
import time
from xianc.config.setings import Config as Config
config=Config()

FAILURES_FILE = config.realreport+os.sep+"failures.txt"


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    print('------------------------------------')

    # 获取钩子方法的调用结果
    out = yield
    print('用例执行结果', out)

    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()

    print('测试报告：%s' % report)
    print('步骤：%s' % report.when)
    print('nodeid：%s' % report.nodeid)
    print("测试结果:%s"%report.outcome)
    print('description:%s' % str(item.function.__doc__))
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     result = outcome.get_result()
#     if result.when == "call" and result.failed:
#         try:
#             with open(str(FAILURES_FILE), "a") as f:
#                 f.write(result.nodeid + "\n")
#         except Exception as e:
#             print("ERROR", e)
#             pass


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    收集测试结果
    """
    print(terminalreporter.stats)
    print("total：", terminalreporter._numcollected)
    print('passed：', len(terminalreporter.stats.get('passed', [])))
    print('failed：', len(terminalreporter.stats.get('failed', [])))
    print('error：', len(terminalreporter.stats.get('error', [])))
    print('skipped：', len(terminalreporter.stats.get('skipped', [])))
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
