[![codecov](https://codecov.io/gh/krylov-sergey-sergeevich/PythonAlgorithmLab/branch/main/graph/badge.svg)](https://codecov.io/gh/{username}/{repo})

# 🐍 Python Algorithm Lab

📚 Этот репозиторий содержит:
- **Теорию** по алгоритмам и структурам данных
- **Практику** решения задач (LeetCode, Codeforces и др.)
- **Заметки** и полезные советы по Python
- **Дневник** решений с разбором задач

## 🗂 Структура

### 📦 Установка и настройка

#### Виртуальное окружение (рекомендуется)

Создайте и активируйте виртуальное окружение:

```bash
# Создание виртуального окружения
python -m venv env_python_algorithm_lab

# Активация окружения
# На Windows:
.\env_python_algorithm_lab\Scripts\activate

# На macOS и Linux:
source env_python_algorithm_lab/bin/activate

# Теперь можно устанавливать пакеты в изолированное окружение
pip install -r requirements.txt
# или установка как локального пакета (-e)
pip install -e .

# Деактивация окружения (когда закончите работать)
deactivate
```

#### Установка зависимостей

**Базовые зависимости (для использования кода):**

```bash
pip install -e .
```

**Для разработки и тестирования:**

```bash
pip install -r requirements-dev.txt
```

**Для CI/CD (если нужно добавить специальные зависимости, например, для отправки покрытия в Codecov):**

```bash
pip install -r requirements-dev.txt codecov
```

#### Установка pre-commit хуков

```bash
pre-commit install
```

### ⚡️ Быстрые команды

**Запуск тестов с замером покрытия:**

```bash
pytest 1_theory/tests/ --cov
```

**Проверка типов:**

```bash
mypy 1_theory/src/
```

**Проверка стиля (PEP 8):**

```bash
flake8 1_theory/src/
```

**Принудительный запуск всех pre-commit хуков:**

```bash
pre-commit run --all-files
```

---