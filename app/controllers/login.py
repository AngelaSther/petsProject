from app import app, db
from flask import render_template, redirect, url_for

from sqlalchemy.exc import IntegrityError
from app.models.table import Tutor, Representante, Instituicao, Ong
from app.models.usersForms import registroTutores, registroRepresentantes, registroInstituicoes, registroOngs

@app.route("/", methods=['POST', 'GET'])
def home():
  return render_template('index.html', home=home)

@app.route("/register-tutor", methods=['POST', 'GET'])
def registroTutor():
  register = registroTutores()

  if registroTutores.validate_on_submit:
    print(register.username.data)

    # CRUD

    try:
      tutor = Tutor(nome_tutor=register.username.data, senha=register.password.data, email=register.email.data, cpf=register.cpf.data, endereco=register.endereco.data)

      if tutor:
        db.session.add(tutor)
        db.session.commit()

        print('Usuário cadastrado')

    except IntegrityError as e:
      db.session.rollback()
      print(f'Erro no banco aqui ó, prestenção: {e}')

  return render_template('register.html', register=register)
