# 🧪 SauceDemo Test Automation Framework

## 📌 Overview
Production-ready test automation framework built with Python + Selenium + PyTest-BDD using Page Object Model design pattern. Covers full e-commerce flow with 29 automated test cases.

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Selenium 4 | Browser automation |
| PyTest | Test runner |
| PyTest-BDD | BDD / Gherkin framework |
| Page Object Model | Design pattern |
| openpyxl / Excel | Data driven testing |
| GitHub Actions | CI/CD pipeline |
| pytest-html | HTML reporting |

## 📁 Project Structure
```
saucedemo-framework/
├── pages/              # Page Object classes
├── features/           # BDD feature files
├── step_definitions/   # Step definitions
├── tests/              # Test runner files
├── utils/              # Helper utilities
├── config/             # Configuration
├── test_data/          # Excel test data
├── reports/            # HTML test reports
└── logs/               # Execution logs
```

## ✅ Test Coverage — 29 Test Cases
| Module | Type | Cases |
|--------|------|-------|
| Login | BDD | 7 |
| Inventory | BDD | 5 |
| Cart | BDD | 5 |
| Checkout | BDD | 5 |
| E2E Journey | BDD | 1 |
| Login | Excel Data Driven | 6 |
| **Total** | | **29** |

## 🚀 How To Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/saucedemo-framework.git
cd saucedemo-framework
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate Excel test data
```bash
python utils/create_test_data.py
```

### 5. Run all tests
```bash
pytest -v
```

### 6. Run specific module
```bash
pytest tests/test_login_bdd.py -v       # Login only
pytest tests/test_e2e.py -v -s          # E2E journey
pytest tests/test_login_excel.py -v     # Excel driven
```

### 7. View report
Open reports/report.html in browser after running.

## 🔄 CI/CD
Tests run automatically on every push via GitHub Actions.
Download test report from Actions → Artifacts after each run.

## 👩‍💻 Author
**Spandita**
4 Years Experience | Test Automation Engineer