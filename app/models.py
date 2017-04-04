from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

article_country_table = db.Table('article_country',
        db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
        db.Column('country_id', db.Integer, db.ForeignKey('country.id')),
)

class Organization(db.Model):
    """
    News source model

    name Name of the source
    description Description of the source
    url Url to the source's website
    logoUrl Url to the source's logo
    articles List of articles belonging to this source
    country Country this source normally reports on
    """
    __tablename__ = 'source'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    logoUrl = db.Column(db.String)

    articles = db.relationship('Article')
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country', back_populates='organization')


    def __repr__(self):
        return '<Organization {0}>'.format(self.country)

class Article(db.Model):
    """
    News article

    title Title of article
    author Author of article
    description Description of article
    publishDate Date article was published
    url Url to article
    imageUrl Url of image associated with article
    organization organization of the article
    countries Countries the article is about
    """
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    description = db.Column(db.String)
    publishDate = db.Column(db.String)
    url = db.Column(db.String)
    imageUrl = db.Column(db.String)

    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    organization = db.relationship('Organization', back_populates='articles')

    countries = db.relationship('Country',
            secondary=article_country_table,
            back_populates='articles')

    def __repr__(self):
        return '<Article {0}>'.format(self.title)


class Country(db.Model):
    """
    Country

    name Name of country
    capital Capital of country
    region Area of the world the country is in
    population Population of country
    flagUrl Url to image of the country's flag
    articles Articles involving the country
    organizations organizations that report on the country
    """
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

    organization = db.relationship('Organizations', back_populates='country')


    def __repr__(self):
        return '<Country {0}>'.format(self.name)
