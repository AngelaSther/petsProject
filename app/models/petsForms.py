from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired

class registroPetMixin(FlaskForm):
  nome = StringField("nome", validators=[DataRequired()])
  especie = StringField("especie", validators=[DataRequired()])
  raca = StringField("raca", validators=[DataRequired()])
  sexo = SelectField("sexo", choices=[('', 'Sexo') ,('masculino', 'Masculino'), ('feminino', 'Feminino')], validators=[DataRequired()])
  idade = IntegerField("idade")
  foto = FileField("Foto")

class registroAdocao(registroPetMixin, FlaskForm):
  situacao = SelectField("situacao", validators=[DataRequired()])
  castrado = BooleanField("castrado", validators=[DataRequired()])
  vacinado = BooleanField("vacinado", validators=[DataRequired()])
  vermifugado = BooleanField("vermifugado", validators=[DataRequired()])
  necessidadesEspeciais = BooleanField("necessidadesEspeciais", validators=[DataRequired()])
  info = StringField("info")
