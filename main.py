from flask import Flask, request
import os

app = Flask(__name__)

# Глобальная переменная для счётчика
visits = 0

# Главная страница
@app.route("/")
def index():
    return """
    <h1>STEPAN</h1>
    <p>Добро пожаловать на наш сайт!</p>
    <p>Вот пара новых страничек для теста:</p>
    <ul>
      <li><a href="/counter">Счётчик посещений</a></li>
      <li><a href="/form">Форма ввода</a></li>
    </ul>
    """

# Счётчик посещений
@app.route("/counter")
def counter():
    global visits
    visits += 1
    return f"Страницу /counter открыли уже {visits} раз(а)."

# Простая HTML-форма
@app.route("/form", methods=["GET", "POST"])
def form_example():
    if request.method == "POST":
        user_input = request.form.get("text_input", "")
        return f"<h3>Вы ввели: {user_input}</h3><p><a href='/form'>Вернуться назад</a></p>"
    else:
        # При GET-запросе отдадим форму
        return """
        <h3>Введите любой текст:</h3>
        <form method="post" action="/form">
            <input type="text" name="text_input" placeholder="Напишите что-нибудь" />
            <button type="submit">Отправить</button>
        </form>
        <p><a href="/">На главную</a></p>
        """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
