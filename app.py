from flask import Flask, request, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    resultado = None

    if request.method == 'POST':
        semanas = int(request.form.get('semanas_input'))

        operacao = request.form.get('operacao')

        if operacao == '(-)':
            semanas_digitadas = timedelta(weeks=semanas)
            data_atual = datetime.now()
            data_antiga = data_atual - semanas_digitadas
            data_antiga_formatada = data_antiga.strftime("%d/%m/%y")
            resultado = data_antiga_formatada
        else:
            semanas_digitadas = timedelta(weeks=semanas)
            data_atual = datetime.now()
            data_antiga = data_atual + semanas_digitadas
            data_antiga_formatada = data_antiga.strftime("%d/%m/%y")
            resultado = data_antiga_formatada
    
    return render_template("index.html", data_final=resultado)

if __name__ == '__main__':
    app.run(debug=True)
