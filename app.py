from flask import Flask, render_template, request

from process import get_prediction


app = Flask(__name__)


@app.route('/', methods=["get", "post"])
def hello():
    message = ""
    if request.method == "POST":
        area = request.form.get("area")
        # TODO: Добавить проверку ввода
        area = float(area)
        cost = get_prediction(area)
        message = f"Стоимость квартиры площадью {area} кв.м. равна {cost} рублей."
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()
