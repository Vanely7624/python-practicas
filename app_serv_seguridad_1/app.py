from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página Quiénes Somos
@app.route('/acerca_de')
def acerca_de():
    return render_template('acerca_de.html')

# Página de Servicios
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

# Página de Noticias
@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

# Página de Contacto
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return render_template('form_data.html', name=name, email=email, message=message)
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)