# Importar Flask y extensiones
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Inicializar app
app = Flask(__name__)

# Configurar conexión a PostgreSQL (asegúrate de usar el puerto correcto)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:LinuxAdmin99$@localhost:5432/devops_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Modelo de la base de datos
class Visitante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

# Ruta principal (index)
@app.route('/')
def index():
    visitantes = Visitante.query.all()
    return render_template("index.html", visitantes=visitantes)

# Ruta para crear nuevos visitantes
@app.route('/crear', methods=['POST'])
def crear():
    nombre = request.form['nombre']
    correo = request.form['correo']

    nuevo = Visitante(nombre=nombre, correo=correo)
    db.session.add(nuevo)
    db.session.commit()

    return redirect(url_for('index'))
# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
