import os, uuid
from app import app, db
from flask import render_template, redirect, url_for, request, session
from werkzeug.utils import secure_filename

from sqlalchemy.exc import IntegrityError
from app.models.petsForms import registroPetMixin
from app.models.table import Pet, Tutor, CartaoVacina

@app.route('/tutor', methods=["GET", "POST"])
def tutores():
  tutorID = session.get('tutor')
  registerPet = registroPetMixin()

  if registerPet.validate_on_submit():
    try:
      arquivo = registerPet.foto.data
      if arquivo:
        nome_seguro = secure_filename(arquivo.filename)
        ext = os.path.splitext(nome_seguro)[1]   # pega extensão
        nome_unico = f"{uuid.uuid4().hex}{ext}"  # gera nome único
        
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_unico)
        arquivo.save(caminho)

        pet = Pet(nome=registerPet.nome.data, especie=registerPet.especie.data, raca=registerPet.raca.data, sexo=registerPet.sexo.data, idade=registerPet.idade.data, foto=nome_unico, id_tutor=tutorID)

        db.session.add(pet)
        db.session.commit()

        return redirect(url_for('tutores'))
      else:
        pet = Pet(nome=registerPet.nome.data, especie=registerPet.especie.data, raca=registerPet.raca.data, sexo=registerPet.sexo.data, idade=registerPet.idade.data, foto=None, id_tutor=tutorID)

        db.session.add(pet)
        db.session.commit()

        return redirect(url_for('tutores'))
      
    except IntegrityError as e:
      db.session.rollback()
      print(f'Erro no banco aqui ó, prestenção: {e}')

    # INFO-PETS

  petInfo = Pet.query.filter(Pet.id_tutor==tutorID).all()
  tutorInfo = Tutor.query.filter(Tutor.id_tutor==tutorID).all()

  return render_template('tutores.html', registerPet=registerPet, petInfo=petInfo)

@app.route('/perfil', methods=["GET", "POST"])
def perfil():
  tutorID = session.get('tutor')
  tipo = request.args.get('tipo')
  cartaoInfo = []

  tutorInfo = Tutor.query.filter(Tutor.id_tutor==tutorID).first()
  petInfo = Pet.query.filter(Pet.nome==tipo).first()

  if petInfo:
    if tipo == petInfo.nome:
      print(petInfo)
      cartaoInfo = CartaoVacina.query.filter(CartaoVacina.id_animal==petInfo.id_pet).all()
  else:
    print('tem não man')

  if tutorInfo:
    print('sei la')
  
  return render_template('tutores-pets-perfil.html', tipo=tipo, tutorInfo=tutorInfo, petInfo=petInfo, cartaoInfo=cartaoInfo)
