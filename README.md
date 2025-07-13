[![codecov](https://codecov.io/gh/krylov-sergey-sergeevich/PythonAlgorithmLab/branch/main/graph/badge.svg)](https://codecov.io/gh/{username}/{repo})

# 🐍 Python Algorithm Lab

📚 Этот репозиторий содержит:  
- **Теорию** по алгоритмам и структурам данных  
- **Практику** решения задач (LeetCode, Codeforces и др.)  
- **Заметки** и полезные советы по Python  
- **Дневник** решений с разбором задач  

## 🗂 Структура
  
### 📦 Установка и настройка

**Базовые зависимости (для использования кода)**

`pip install -e .`

**Для разработки и тестирования**

`pip install -r .\requirements-dev.txt`

**Для CI/CD (если нужно добавить спец. зависимости)**

`pip install -r requirements-dev.txt codecov` - _для отправки coverage в Codecov_

**Установка pre-commit хуков**

`pip pre-commit install`
  
### ⚡️ Быстрые команды

**Запуск тестов с замером покрытия**
```
pytest 1_theory/tests/ --cov
```

**Проверка типов**
```
mypy 1_theory/src/
```

**Проверка стиля (PEP 8)**
```
flake8 1_theory/src/
```

**Принудительный запуск pre-commit**
```
pre-commit run --all-files	
```