from flask import Flask, request, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    resultado = None

    if request.method == 'POST':
        tipo = request.form.get('tipo')

        if tipo == 'semana':    
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

        elif tipo == 'dia':
            dias = int(request.form.get('semanas_input'))

            operacao = request.form.get('operacao')

            if operacao == '(-)':
                dias_digitadas = timedelta(days=dias)
                data_atual = datetime.now()
                data_antiga = data_atual - dias_digitadas
                data_antiga_formatada = data_antiga.strftime("%d/%m/%y")
                resultado = data_antiga_formatada
            else:
                dias_digitadas = timedelta(days=dias)
                data_atual = datetime.now()
                data_antiga = data_atual + dias_digitadas
                data_antiga_formatada = data_antiga.strftime("%d/%m/%y")
                resultado = data_antiga_formatada

        elif tipo == 'mes':
            mes = int(request.form.get('semanas_input'))

            operacao = request.form.get('operacao')

            if operacao == '(-)':
                mes_digitado = mes * timedelta(days=30)
                data_atual = datetime.now()
                data_antiga = data_atual - mes_digitado
                data_antiga_formatada = data_antiga.strftime("%d/%m/%y")
                resultado = data_antiga_formatada
            else:
                mes_digitado = mes * timedelta(days=30)
                data_atual = datetime.now()
                data_antiga = data_atual + mes_digitado
                data_antiga_formatada = data_antiga.strftime("%d/%m/%y")
                resultado = data_antiga_formatada
        
        elif tipo == 'ano':
            ano = int(request.form.get('semanas_input'))

            operacao = request.form.get('operacao')

            if operacao == '(-)':
                ano_digitadas = ano * timedelta(days=365)
                data_atual = datetime.now()
                data_antiga = data_atual - ano_digitadas
                data_antiga_formatada = data_antiga.strftime("%d/%m/%y")
                resultado = data_antiga_formatada
            else:
                ano_digitadas = ano * timedelta(days=365)
                data_atual = datetime.now()
                data_antiga = data_atual + ano_digitadas
                data_antiga_formatada = data_antiga.strftime("%d/%m/%y")
                resultado = data_antiga_formatada
    
    return render_template("index.html", data_final=resultado)

if __name__ == '__main__':
    app.run(debug=True)
