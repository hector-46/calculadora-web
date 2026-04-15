from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operacion = request.form.get("operacion")

        if num1 and num2:
            a = int(num1)
            b = int(num2)

            if operacion == "suma":
                resultado = a + b
            elif operacion == "resta":
                resultado = a - b
            elif operacion == "multiplicacion":
                resultado = a * b
            elif operacion == "division":
                resultado = a / b if b != 0 else "Error"

            # Operaciones binarias
            elif operacion == "and":
                resultado = a & b
            elif operacion == "or":
                resultado = a | b
            elif operacion == "xor":
                resultado = a ^ b

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    