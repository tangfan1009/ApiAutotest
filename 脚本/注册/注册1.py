import openpyxl
workbook = openpyxl.load_workbook("D:\ApiAutoTest\脚本\注册\login_fail.xlsx")
worksheet = workbook["failed"]
file = [tuple(cell.value for cell in row) for row in worksheet][1:]
print(file)