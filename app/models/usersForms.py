from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired

# BASES PARA REGISTRO

class registroPessoasMixin():
  username = StringField("username", validators=[DataRequired()])
  email = StringField("email", validators=[DataRequired()])
  cpf = IntegerField("cpf", validators=[DataRequired()])

class registroOrganizacoesMixin():
  nome = StringField("nome", validators=[DataRequired()])
  email = StringField("email", validators=[DataRequired()])
  cnpj = IntegerField("cnpj")
  password = PasswordField('password', validators=[DataRequired()])
  endereco = StringField("endereco", validators=[DataRequired()])

# REGISTRO PESSOAS

class registroTutores(registroPessoasMixin, FlaskForm):
  endereco = StringField("endereco", validators=[DataRequired()])
  password = PasswordField("password", validators=[DataRequired()])

class registroRepresentantes(registroPessoasMixin ,FlaskForm):
  tipo = StringField("tipo", validators=[DataRequired()])
  id_organizacao = IntegerField('id_organizacao', validators=[DataRequired()])

# REGISTRO ORGANIZAÇÕES

class registroOngs(registroOrganizacoesMixin, FlaskForm):
  membros_num = IntegerField("membros_num")
  animais_num = IntegerField("animais_num")

class registroInstituicoes(registroOrganizacoesMixin, FlaskForm):
  tipo = StringField("tipo", validators=[DataRequired()])

# LOGIN

class login(FlaskForm):
  email = StringField("email", validators=[DataRequired()])
  password = PasswordField("password", validators=[DataRequired()])