import math
from flask import render_template, request

def calcular():
    try:
        num1 = float(request.form["num1"])
        operacao = request.form["operacao"]

        resultado = ""
        etapas = ""

        if operacao == "sqrt":
            if num1 < 0:
                resultado = "Erro"
                etapas = "Não existe raiz quadrada de número negativo."
            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1} = {resultado}"

        elif operacao == "log":
            if num1 <= 0:
                resultado = "Erro"
                etapas = "Logaritmo só existe para números positivos."
            else:
                resultado = math.log(num1)
                etapas = f"log({num1}) = {resultado}"

        else:
            num2_valor = request.form.get("num2", "").strip()

            if not num2_valor:
                return render_template(
                    "calculadora.html",
                    etapas="Informe o segundo número.",
                    resultados=""
                )

            num2 = float(num2_valor)

            if operacao == "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2} = {resultado}"

            elif operacao == "-":
                resultado = num1 - num2
                etapas = f"{num1} - {num2} = {resultado}"

            elif operacao == "*":
                resultado = num1 * num2
                etapas = f"{num1} × {num2} = {resultado}"

            elif operacao == "/":
                if num2 == 0:
                    resultado = "Erro"
                    etapas = "Não é possível dividir por zero."
                else:
                    resultado = num1 / num2
                    etapas = f"{num1} ÷ {num2} = {resultado}"

            elif operacao == "**":
                resultado = math.pow(num1, num2)
                etapas = f"{num1}^{num2} = {resultado}"

        return render_template(
            "calculadora.html",
            etapas=etapas,
            resultados=resultado
        )

    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Digite valores válidos.",
            resultados=""
        )