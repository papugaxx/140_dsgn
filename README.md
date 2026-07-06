# Design Flow

Учебный Django-проект, доведённый до портфолио-уровня: сайт дизайн-студии с витриной услуг, портфолио, регистрацией клиентов, личным кабинетом и заказами с файлами.

<img width="1353" height="917" alt="Снимок экрана 2026-07-06 135908" src="https://github.com/user-attachments/assets/ac2bbd9f-45fe-4816-a83a-40260f45839a" />

<img width="1406" height="832" alt="Снимок экрана 2026-07-06 135902" src="https://github.com/user-attachments/assets/1b2632a4-b033-4ae9-bc47-aa32ddbe31ae" />

<img width="1362" height="883" alt="Снимок экрана 2026-07-06 140008" src="https://github.com/user-attachments/assets/cc1a8ade-225d-45cb-8f37-101777b51446" />

<img width="1326" height="931" alt="Снимок экрана 2026-07-06 140014" src="https://github.com/user-attachments/assets/1daba5e0-ccd9-4985-b8f7-383a0d0653db" />

<img width="1367" height="799" alt="Снимок экрана 2026-07-06 140021" src="https://github.com/user-attachments/assets/f2c48553-72a9-4bd3-bc42-65cd1a12778a" />


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
