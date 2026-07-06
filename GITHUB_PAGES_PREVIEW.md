# GitHub Pages preview

`docs/` — статическое GitHub Pages превью, собранное как визуальное зеркало текущего Django-сайта.

Что важно:

- разметка повторяет текущие Django-страницы;
- используется та же Bootstrap-навигация;
- используется тот же CSS: `static/css/style.css` скопирован в `docs/static/css/site.css`;
- страницы сделаны статическими, поэтому авторизация, админка, база данных, отправка форм и загрузка файлов не работают в GitHub Pages.

## Как включить GitHub Pages

1. Залей проект в GitHub.
2. Открой `Settings` → `Pages`.
3. Выбери:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/docs`
4. Сохрани.

GitHub Pages откроет `docs/index.html`.
