from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# 1. Главная страница (как и раньше)
@app.route("/")
def index():
    return "STEPAN"

# 2. Страница «Приветствие» (с передачей параметра)
@app.route("/hello/<name>")
def hello(name):
    return f"Привет, {name}!"

# 3. Пример простой HTML-страницы с использованием render_template_string
# (в реальном проекте лучше использовать render_template и отдельные .html-файлы)
@app.route("/info")
def info():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Info Page</title>
    </head>
    <body>
        <h1>Добро пожаловать на информационную страницу!</h1>
        <p>Здесь мы можем разместить какую-то информацию о нашем проекте.</p>
        <a href="/">На главную</a>
    </body>
    </html>
    """
    return render_template_string(html_content)

# 4. Страница с формой (GET и POST)
@app.route("/form", methods=["GET", "POST"])
def form_example():
    if request.method == "POST":
        user_input = request.form.get("text_input", "")
        return f"Вы ввели: {user_input}"
    else:
        # При GET-запросе показываем HTML-форму
        form_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Форма ввода</title>
        </head>
        <body>
            <h1>Введите что-нибудь:</h1>
            <form method="post" action="/form">
                <input type="text" name="text_input" placeholder="Ваш текст" />
                <button type="submit">Отправить</button>
            </form>
            <a href="/">На главную</a>
        </body>
        </html>
        """
        return render_template_string(form_html)

# 5. Немного динамического контента: счётчик посещений
# Для упрощённого хранения счётчика используем глобальную переменную
visits = 0

@app.route("/counter")
def counter():
    global visits
    visits += 1
    return f"Эту страницу просмотрели {visits} раз(а)."

# Запуск приложения
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
