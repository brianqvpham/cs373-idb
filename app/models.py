from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

article_country_table = db.Table('article_country',
        db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
        db.Column('country_id', db.Integer, db.ForeignKey('country.id')),
)

class Source(db.Model):
    __tablename__ = 'source'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    logoUrl = db.Column(db.String)

    def __repr__(self):
        return '<Source {0}>'.format(self.name)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    imageUrl = db.Column(db.String)

    countries = db.relationship('Country',
            secondary=article_country_table,
            back_populates='articles')

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    articles = db.relationship('Article',
            secondary=article_country_table,
            back_populates='countries')

