from app import app, db
from flask import render_template, redirect, url_for, request, session

from sqlalchemy.exc import IntegrityError
from app.models.petsForms import registroPetMixin
from app.models.table import Pet

@app.route('/tutor', methods=["GET", "POST"])
def tutores():
  tutorID = session.get('tutor')
  registerPet = registroPetMixin()

  if registerPet.validate_on_submit():
    try:
      pet = Pet(nome=registerPet.nome.data, especie=registerPet.especie.data, raca=registerPet.raca.data, sexo=registerPet.sexo.data, idade=registerPet.idade.data, foto=None, id_tutor=tutorID)

      db.session.add(pet)
      db.session.commit()

      return redirect(url_for('tutores'))
      
    except IntegrityError as e:
      db.session.rollback()
      print(f'Erro no banco aqui ó, prestenção: {e}')

  return render_template('tutores.html', registerPet=registerPet)
