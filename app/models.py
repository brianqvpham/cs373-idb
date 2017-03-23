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

    articles = db.relationship('Article')
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country', back_populates='sources')

    def __repr__(self):
        return '<Source {0}>'.format(self.country)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    imageUrl = db.Column(db.String)

    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    source = db.relationship('Source', back_populates='articles')

    countries = db.relationship('Country',
            secondary=article_country_table,
            back_populates='articles')

    def __repr__(self):
        return '<Article {0}>'.format(self.title)

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    capital = db.Column(db.String)
    region = db.Column(db.String)
    population = db.Column(db.Integer)
    flagUrl = db.Column(db.String)

    articles = db.relationship('Article',
            secondary=article_country_table,
            back_populates='countries')

    sources = db.relationship('Source', back_populates='country')

    def __repr__(self):
        return '<Country {0}>'.format(self.name)

