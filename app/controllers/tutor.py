import os, uuid
from app import app, db
from flask import render_template, redirect, url_for, request, session
from werkzeug.utils import secure_filename

from sqlalchemy.exc import IntegrityError
from app.models.petsForms import registroPetMixin
from app.models.table import Pet

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

  # petInfo = Pet.query.filter(Pet.nome.isnot(None), Pet.foto.isnot(None)).all()
  petInfo = Pet.query.filter(Pet.id_tutor==tutorID).all()
  print(petInfo)

  return render_template('tutores.html', registerPet=registerPet, petInfo=petInfo)
