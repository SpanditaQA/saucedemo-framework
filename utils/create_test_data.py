import openpyxl
import os

def create_login_data():
    os.makedirs("test_data", exist_ok=True)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "LoginData"

    # Column headers
    ws.append(["username", "password", "expected_result"])

    # ✅ Should PASS (valid users)
    ws.append(["standard_user",           "secret_sauce", "pass"])
    ws.append(["performance_glitch_user", "secret_sauce", "pass"])

    # ❌ Should FAIL (invalid users)
    ws.append(["wrong_user",      "wrong_pass",   "fail"])
    ws.append(["locked_out_user", "secret_sauce", "fail"])
    ws.append(["standard_user",   "",             "fail"])
    ws.append(["",                "secret_sauce", "fail"])

    wb.save("test_data/login_data.xlsx")
    print("✅ Excel file created: test_data/login_data.xlsx")

if __name__ == "__main__":
    create_login_data()