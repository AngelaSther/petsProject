from app import app, db
from flask import render_template, redirect, url_for, request, session

from sqlalchemy.exc import IntegrityError
from app.models.table import Tutor, Representante, Instituicao, Ong
from app.models.usersForms import registroTutores, registroRepresentantes, registroInstituicoes, registroOngs, login

@app.route("/", methods=['POST', 'GET'])
def home():
  return render_template('index.html')

@app.route("/register", methods=['POST', 'GET'])
def registro():
  tipo = request.args.get('tipo')

  register = registroTutores()
  registerOng = registroOngs()
  registerInstituicao = registroInstituicoes()
  login_form = login()

  # REGISTRO TUTORES

  if register.validate_on_submit() and request.form.get("form_type") == "tutor":
      print(register.username.data)
      
      try:
        tutor = Tutor(nome_tutor=register.username.data, senha=register.password.data, email=register.email.data, cpf=register.cpf.data, endereco=register.endereco.data)

        if tutor:
          db.session.add(tutor)
          db.session.commit()

          print('Usuário cadastrado')
          tipo = 'login'

      except IntegrityError as e:
        db.session.rollback()
        print(f'Erro no banco aqui ó, prestenção: {e}')


  # REGISTRO ONG

  elif registerOng.validate_on_submit() and request.form.get("form_type") == "ong": 
    try:
      ong = Ong(nome=registerOng.nome.data, email=registerOng.email.data, senha=registerOng.password.data,cnpj=registerOng.cnpj.data, endereco=registerOng.endereco.data, animais_num=registerOng.animais_num.data, membros_num=registerOng.membros_num.data)
      db.session.add(ong)
      db.session.commit()
      print('ong cadastrada')
      tipo = 'login'
    
    except IntegrityError as e:
      db.session.rollback()
      print(f'Erro no banco aqui ó, prestenção: {e}')


  # REGISTRO INSTITUIÇÕES

  elif registerInstituicao.validate_on_submit() and request.form.get("form_type") == "instituicao":
    try:
      instituicao = Instituicao(nome=registerInstituicao.nome.data, email=registerInstituicao.email.data, senha=registerInstituicao.password.data, cnpj=registerInstituicao.cnpj.data, endereco=registerInstituicao.endereco.data, tipo=registerInstituicao.tipo.data)

      db.session.add(instituicao)
      db.session.commit()

      print('instituição cadastrada')
      tipo = 'login'

    except IntegrityError as e:
      db.session.rollback()
      print(f'Erro no banco aqui ó, prestenção: {e}')


  # LOGIN

  elif login_form.validate_on_submit() and request.form.get("form_type") == "login":
    try:
      validarTutor = Tutor.query.filter_by(email=login_form.email.data, senha=login_form.password.data).first()
      validarOng = Ong.query.filter_by(email=login_form.email.data, senha=login_form.password.data).first()
      validarInstituicao = Instituicao.query.filter_by(email=login_form.email.data, senha=login_form.password.data).first()

      if validarTutor:
        print('deu certo!')

        session['tutor']=validarTutor.id_tutor
        return redirect(url_for('tutores'))
      elif validarOng:
        print('Ong validada!')
        # return redirect(url_for('tutores'))
      elif validarInstituicao:
        print('instituição validada!')
        # return redirect(url_for('tutores'))
      else:
        print('viushh')

    except IntegrityError as e:
      db.session.rollback()
      print(f'Erro no banco aqui ó, prestenção: {e}')

  return render_template('register.html', register=register, registerOng=registerOng, registerInstituicao=registerInstituicao, login_form=login_form, tipo_modal=tipo)
