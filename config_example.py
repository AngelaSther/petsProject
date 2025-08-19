class Config:
  DEBUG = True

  SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost:5432/database"
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  SECRET_KEY = 'sua_secret_key'