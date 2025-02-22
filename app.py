from flask import Flask, render_template, request

from process import get_prediction


app = Flask(__name__)


@app.route('/', methods=["get", "post"])
def hello():
    message = ""
    if request.method == "POST":
        area = request.form.get("area")
        try:
            area = float(area)
        except Exception as e:
            print(e)
            message += "Некорректный ввод. Установлено значение по умолчанию: 0 кв.м."
            area = 0.0
        cost = get_prediction(area)
        message += f"Стоимость квартиры площадью {area} кв.м. равна {cost} рублей."
    return render_template("index.html", message=message)

