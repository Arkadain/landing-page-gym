from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # Esto busca automáticamente el index.html en la carpeta templates
    return render_template('index.html')

if __name__ == '__main__':
    # El debug=True hace que la página se actualice sola cuando cambiás el HTML
    app.run(debug=True)