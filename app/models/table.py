from app import db
from sqlalchemy.dialects.postgresql import ENUM

class Tutor(db.Model):
  __tablename__ = "tutores"

  id_tutor = db.Column(db.Integer, primary_key=True)
  nome_tutor = db.Column(db.String(80), nullable=False)
  senha = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  cpf = db.Column(db.Integer, unique=True, nullable=False)
  endereco = db.Column(db.String, nullable=False)

  def __init__(self, nome_tutor, senha, email, cpf, endereco):
    self.nome_tutor = nome_tutor
    self.senha = senha
    self.email = email
    self.cpf = cpf
    self.endereco = endereco

  def __repr__(self):
    return "<Nome do tutor: %r>" % self.username

class Pet(db.Model):
  __tablename__ = "pets"

  id_pet = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  especie = db.Column(db.String, nullable=False)
  raca = db.Column(db.String)
  sexo = db.Column(db.String, nullable=False)
  idade = db.Column(db.Integer)
  foto = db.Column(db.String)

  id_tutor = db.Column(db.Integer, db.ForeignKey('tutores.id_tutor'))
  tutor = db.relationship('Tutor', foreign_keys=id_tutor)

  def __init__(self, nome, especie, raca, sexo, idade, foto, id_tutor):
    self.nome = nome
    self.especie = especie
    self.raca = raca
    self.sexo = sexo
    self.idade = idade
    self.foto = foto
    self.id_tutor = id_tutor

  def __repr__(self):
    return "<Nome do pet: %r>" % self.nome_pet

tipo_enum = ENUM(
  'ong', 'instituicao',
  name='tipo_enum',
  create_type=True
)

class Representante(db.Model):
  __tablename__ = "representantes"

  id_representante = db.Column(db.Integer, primary_key=True)
  nome_rep = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String, nullable=False, unique=True)
  cpf = db.Column(db.Integer, unique=True, nullable=False)
  tipo = db.Column(db.String, tipo_enum, nullable=False)
  id_organizacao = db.Column(db.Integer, nullable=False)

  def __init__(self, nome_rep, email, cpf, tipo, id_organizacao):
    self.nome_rep = nome_rep
    self.email = email
    self.cpf = cpf
    self.tipo = tipo
    self.id_organizacao = id_organizacao

  def __repr__(self):
    return "<Nome representante: %r>" % self.nome_rep
  
class Instituicao(db.Model):
  __tablename__ = "instituicoes"

  id_instituicao = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String, nullable=False, unique=True)
  senha = db.Column(db.String, nullable=False)
  cnpj = db.Column(db.Integer, nullable=False, unique=True)
  endereco = db.Column(db.String, nullable=False)
  tipo = db.Column(db.String, nullable=False)
  
  def __init__(self, nome, email, senha, cnpj, endereco, tipo):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.cnpj = cnpj
    self.endereco = endereco
    self.tipo = tipo
  
  def __repr__(self):
    return "<Nome instituicao: %r>" % self.nome
  
class Ong(db.Model):
  __tablename__ = "ongs"

  id_ong = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String, nullable=False, unique=True)
  senha = db.Column(db.String, nullable=False)
  cnpj = db.Column(db.Integer, unique=True)
  endereco = db.Column(db.String, nullable=False)
  membros_num = db.Column(db.Integer, nullable=True)
  animais_num = db.Column(db.Integer, nullable=True)
  
  def __init__(self, nome, email, senha, cnpj, endereco, membros_num, animais_num):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.cnpj = cnpj
    self.endereco = endereco
    self.membros_num = membros_num
    self.animais_num = animais_num
  
  def __repr__(self):
    return "<Nome ong: %r>" % self.nome
  
class Campanha(db.Model):
  __tablename__ = "campanhas"

  id_campanha = db.Column(db.Integer, primary_key=True)
  organizacao = db.Column(db.String, nullable=False)
  titulo = db.Column(db.String(80), nullable=False)
  endereco = db.Column(db.String, nullable=False)
  data = db.Column(db.Integer) # arrumar a data aqui
  hora = db.Column(db.Integer, nullable=False)
  tipo = db.Column(db.Integer, nullable=False)
  conteudo = db.Column(db.String, nullable=False)
  foto = db.Column(db.String)
  
  def __init__(self, titulo, endereco, data, hora, tipo, conteudo, foto, organizacao):
    self.titulo = titulo
    self.endereco = endereco
    self.data = data
    self.hora = hora
    self.tipo = tipo
    self.conteudo = conteudo
    self.foto = foto
    self.organizacao = organizacao

  def __repr__(self):
    return "<Nome campanha: %r>" % self.titulo

sim_nao_enum = ENUM(
  'sim', 'nao',
  name='sim_nao_enum',
  create_type=True
)

class Adocao(db.Model):
  __tablename__ = "adocoes"

  id_adocao = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  especie = db.Column(db.String, unique=True, nullable=False)
  raca = db.Column(db.Integer)
  sexo = db.Column(db.String, nullable=False)
  idade = db.Column(db.Integer)
  foto = db.Column(db.String)
  castrado = db.Column(db.String, sim_nao_enum, nullable=False)
  vacinado = db.Column(db.String, sim_nao_enum, nullable=False)
  vermifugado = db.Column(db.String, sim_nao_enum, nullable=False)
  necessidades_especiais = db.Column(db.String, sim_nao_enum, nullable=False)
  situacao = db.Column(db.String, nullable=False)
  adc_info = db.Column(db.String, nullable=False)

  id_ong = db.Column(db.Integer, db.ForeignKey('ongs.id_ong'))
  ong = db.relationship('Ong', foreign_keys=id_ong)
  
  def __init__(self, nome, especie, raca, sexo, idade, foto, castrado, vacinado, vermifugado, necessidades_especiais, situacao, adc_info, id_ong):
    self.nome = nome
    self.especie = especie
    self.raca = raca
    self.sexo = sexo
    self.idade = idade
    self.foto = foto
    self.castrado = castrado
    self.vacinado = vacinado
    self.vermifugado = vermifugado
    self.necessidades_especiais = necessidades_especiais
    self.situacao = situacao
    self.adc_info = adc_info
    self.id_ong
  
  def __repr__(self):
    return "<Nome adocao: %r>" % self.nome

class CartaoVacina(db.Model):
  __tablename__ = "cartao_vacina"

  id_cartao = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  dose = db.Column(db.String, nullable=False)
  data = db.Column(db.Integer) # arrumar a data aqui
  data_reforco = db.Column(db.Integer) # arrumar a data aqui
  lote = db.Column(db.Integer, nullable=False)
  assinatura = db.Column(db.String, nullable=False)
  obs = db.Column(db.String)
  id_animal = db.Column(db.String, nullable=False, unique=True)
  
  def __init__(self, nome, dose, data, data_reforco, lote, assinatura, obs, id_animal):
    self.nome = nome
    self.dose = dose
    self.data = data
    self.data_reforco = data_reforco
    self.lote = lote
    self.assinatura = assinatura
    self.obs = obs
    self.id_animal = id_animal

  def __repr__(self):
    return "<Nome vacina: %r>" % self.nome
  
# talvez criar um enum para por os id dos animais para o cartao de vacinas e os id das ongs e instituicoes para as campanhas, reduzir as opcoes para apenas essas duas Nao da certo