# 🏨 Hotel Booking API (FastAPI)

## 📌 Описание
Этот проект представляет собой API на основе FastAPI для бронирования номеров в отеле.  
Позволяет пользователям искать доступные номера, бронировать их и управлять своими бронированиями.

## 🚀 Функциональность
- 🔹 Регистрация и аутентификация пользователей (JWT)  
- 🔹 Просмотр доступных номеров  
- 🔹 Бронирование номеров  
- 🔹 Управление бронированиями (отмена, изменение)  
- 🔹 Административные функции (добавление/редактирование номеров)  

## 🛠️ Технологии
- 🐍 Python 3.9+  
- ⚡ FastAPI  
- 🗄️ SQLAlchemy (PostgreSQL)  
- 🔄 Alembic (миграции)  
- ✅ Pydantic (валидация)  
- 🔐 JWT (аутентификация)  
- 🐳 Docker (опционально)  

---

## 📦 Установка и запуск

### 1️⃣ Клонирование репозитория
```sh
git clone https://github.com/your-repo/hotel-booking-api.git
cd hotel-booking-api
```

###Установка зависимостей
```
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```

###Настройка переменных окружения
```
DATABASE_URL=postgresql://user:password@localhost/db_name
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30

```

###Запуск базы данных (если используется Docker)
```
docker-compose up -d
```

###Запуск сервера FastAPI
```cmd
fastapi dev main.py
```
