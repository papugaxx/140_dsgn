# Design Flow

Учебный Django-проект, доведённый до портфолио-уровня: сайт дизайн-студии с витриной услуг, портфолио, регистрацией клиентов, личным кабинетом и заказами с файлами.

## Возможности

- Минималистичный тёмно-светлый интерфейс в стиле современной digital-студии
- Главная, услуги, портфолио, страница проекта и контакты
- Полностью управляемый контент через Django Admin:
  - тексты сайта, hero-блок, статистика, CTA, контакты и SEO-описание
  - услуги, цены, сроки и изображения
  - категории и кейсы портфолио
  - заказы, статусы, цена, дедлайн, комментарии и финальные файлы
- Регистрация, вход, личный кабинет клиента
- Загрузка материалов к заказу с ограничениями по типу, размеру и количеству файлов
- Демо-данные и demo preview для GitHub Pages
- Dockerfile, docker-compose, Makefile и GitHub Actions CI

## Быстрый запуск

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Открой: http://127.0.0.1:8000/

Демо-пользователи после `seed_demo`:

- Админ: `admin` / `AdminPass2026!`
- Клиент: `client` / `ClientPass2026!`

## Docker

```bash
cp .env.example .env
docker compose up --build
```

По умолчанию compose хранит SQLite и media-файлы в Docker volumes.

## Админка

Админ-панель доступна по адресу `/admin/`. Основные сущности:

- **Настройки сайта** — весь текст главной, контактов, CTA, SEO и футера
- **Услуги** — карточки услуг, цены, сроки, изображения
- **Портфолио** — категории и работы
- **Заказы** — статусы, стоимость, дедлайны, комментарии дизайнера, финальный файл

## GitHub Pages

GitHub Pages не запускает Django/Python, поэтому в проекте есть статический preview в папке `docs/` и workflow `.github/workflows/pages.yml`.

Чтобы включить preview:

1. Запушь проект на GitHub.
2. Открой **Settings → Pages**.
3. В **Build and deployment** выбери **GitHub Actions**.
4. После push в `main` или `master` GitHub Pages опубликует `docs/`.

Полное приложение запускается локально или на хостинге с Python/Docker.

## Проверки

```bash
python manage.py check
python manage.py test
```

CI запускает эти команды на GitHub Actions.

## Стек

- Python 3.12+
- Django 5
- SQLite для локального запуска
- Bootstrap 5 + кастомный CSS
- Docker / Docker Compose
