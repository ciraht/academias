from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/Templates/calculadora_imc.html')
def calculadora():
    return render_template('calculadora_imc.html',resultado="Seu resultado aparecerá aqui.", comentario="Uma mensagem aparecerá aqui.")

@app.route('/resultado',methods=['POST'])
def resultado():
    idade = int(request.form['idade'])
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])

    imc = (peso / (altura * altura))

    if imc < 16:
        return render_template('calculadora_imc.html',comentario="Seu estado é de Magreza grave\nProcure um médico ou nutricionista.")
    elif imc < 17:
        return render_template('calculadora_imc.html',comentario="Seu estado é de Magreza moderada\nPrecisa rever sua alimentação.")
    elif imc < 18.5:
        return render_template('calculadora_imc.html',comentario="Seu estado é de Magreza leve\nPrecisa rever sua alimentação.")
    elif imc < 25:
        return render_template('calculadora_imc.html',comentario="Você está Saudável.\nParabéns!")
    elif imc < 30:
        return render_template('calculadora_imc.html',comentario="Seu estado é de Sobrepeso\nPrecisa rever sua alimentação.")
    elif imc < 35:
        return render_template('calculadora_imc.html',comentario="Seu estado é de Obesidade Grau I\nProcure um médico ou nutricionista.")
    elif imc < 40:
        return render_template('calculadora_imc.html',comentario="Seu estado é de Obesidade Grau II (severa)\nProcure um médico ou nutricionista.")
    else:
        return render_template('calculadora_imc.html',comentario="Seu estado é de Obesidade Grau III (mórbida)\nProcure um médico ou nutricionista.")
    
    return render_template('calculadora_imc.html',resultado=f'{imc} kg')

if __name__ =='__main__':
    app.run(debug=True)