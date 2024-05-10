from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculadora_imc')
def calculadora():
    return render_template('calculadora_imc.html',resultado="Seu resultado aparecerá aqui.", comentario="Uma mensagem aparecerá aqui.")

@app.route('/resultado', methods=['POST'])
def resultado():
    idade = int(request.form['idade'])
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])

    imc = peso / (altura * altura)

    if imc < 16:
        comentario = "Seu estado é de Magreza grave. Procure um médico ou nutricionista."
    elif imc < 17:
        comentario = "Seu estado é de Magreza moderada. Precisa rever sua alimentação."
    elif imc < 18.5:
        comentario = "Seu estado é de Magreza leve. Precisa rever sua alimentação."
    elif imc < 25:
        comentario = "Você está Saudável. Parabéns!"
    elif imc < 30:
        comentario = "Seu estado é de Sobrepeso. Precisa rever sua alimentação."
    elif imc < 35:
        comentario = "Seu estado é de Obesidade Grau I. Procure um médico ou nutricionista."
    elif imc < 40:
        comentario = "Seu estado é de Obesidade Grau II (severa). Procure um médico ou nutricionista."
    else:
        comentario = "Seu estado é de Obesidade Grau III (mórbida). Procure um médico ou nutricionista."

    return render_template('calculadora_imc.html', comentario=comentario)


if __name__ =='__main__':
    app.run(debug=True)