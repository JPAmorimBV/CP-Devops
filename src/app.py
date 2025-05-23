from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
import os

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'postgresql://dimdim:senha123@dimdim-db:5432/dimdimapp')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo Cliente
class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'cpf': self.cpf
        }

# Criar tabelas
with app.app_context():
    db.create_all()

# Rota de teste
@app.route('/', methods=['GET'])
def home():
    return make_response(jsonify({'message': 'DimDim App - API REST funcionando!'}), 200)

# CREATE - Criar cliente
@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        if not data or not data.get('nome') or not data.get('email') or not data.get('cpf'):
            return make_response(jsonify({'erro': 'Nome, email e CPF são obrigatórios'}), 400)
        
        novo_cliente = Cliente(
            nome=data['nome'],
            email=data['email'],
            telefone=data.get('telefone'),
            cpf=data['cpf']
        )
        
        db.session.add(novo_cliente)
        db.session.commit()
        
        return make_response(jsonify({
            'mensagem': 'Cliente criado com sucesso',
            'cliente': novo_cliente.json()
        }), 201)
        
    except Exception as e:
        return make_response(jsonify({'erro': f'Erro ao criar cliente: {str(e)}'}), 500)

# READ - Listar todos os clientes
@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    try:
        clientes = Cliente.query.all()
        return make_response(jsonify({
            'clientes': [cliente.json() for cliente in clientes],
            'total': len(clientes)
        }), 200)
    except Exception as e:
        return make_response(jsonify({'erro': f'Erro ao buscar clientes: {str(e)}'}), 500)

# READ - Buscar cliente por ID
@app.route('/api/clientes/<int:id>', methods=['GET'])
def get_cliente(id):
    try:
        cliente = Cliente.query.filter_by(id=id).first()
        if cliente:
            return make_response(jsonify({'cliente': cliente.json()}), 200)
        return make_response(jsonify({'erro': 'Cliente não encontrado'}), 404)
    except Exception as e:
        return make_response(jsonify({'erro': f'Erro ao buscar cliente: {str(e)}'}), 500)

# UPDATE - Atualizar cliente
@app.route('/api/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    try:
        cliente = Cliente.query.filter_by(id=id).first()
        if not cliente:
            return make_response(jsonify({'erro': 'Cliente não encontrado'}), 404)
        
        data = request.get_json()
        if not data:
            return make_response(jsonify({'erro': 'Dados não fornecidos'}), 400)
        
        # Atualizar campos
        if 'nome' in data:
            cliente.nome = data['nome']
        if 'email' in data:
            cliente.email = data['email']
        if 'telefone' in data:
            cliente.telefone = data['telefone']
        if 'cpf' in data:
            cliente.cpf = data['cpf']
        
        db.session.commit()
        
        return make_response(jsonify({
            'mensagem': 'Cliente atualizado com sucesso',
            'cliente': cliente.json()
        }), 200)
        
    except Exception as e:
        return make_response(jsonify({'erro': f'Erro ao atualizar cliente: {str(e)}'}), 500)

# DELETE - Deletar cliente
@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    try:
        cliente = Cliente.query.filter_by(id=id).first()
        if not cliente:
            return make_response(jsonify({'erro': 'Cliente não encontrado'}), 404)
        
        db.session.delete(cliente)
        db.session.commit()
        
        return make_response(jsonify({'mensagem': 'Cliente deletado com sucesso'}), 200)
        
    except Exception as e:
        return make_response(jsonify({'erro': f'Erro ao deletar cliente: {str(e)}'}), 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
