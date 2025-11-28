import os

def run_tests():
    print("开始执行测试...")
    
    # 执行pytest命令
    pytest_cmd = "pytest -v -s --alluredir=./report/allure-results --html=./report/html_report.html --self-contained-html"
    result1 = os.system(pytest_cmd)
    
    if result1 == 0:
        print("pytest测试执行成功")
    else:
        print("pytest测试执行失败")
        return
    
    # 执行allure命令
    print("生成Allure报告...")
    allure_cmd = r"E:\app\allure\allure-2.35.1\bin\allure.bat generate ./report/allure-results -o ./report/allure-html --clean"
    result2 = os.system(allure_cmd)
    
    if result2 == 0:
        print("Allure报告生成成功")
    else:
        print("Allure报告生成失败")

if __name__ == "__main__":
    run_tests()
    
"""
echo [步骤5] 运行测试
pytest -v -s --alluredir=./allure-results --html=./report/html_report.html --self-contained-html
echo [步骤6] 生成Allure报告
E:\app\allure\allure-2.35.1\bin\allure.bat generate ./allure-results -o ./allure-report --clean
"""