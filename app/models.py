from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

db = SQLAlchemy()
ma = Marshmallow()

article_country_table = db.Table('article_country',
        db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
        db.Column('country_id', db.Integer, db.ForeignKey('country.id')),
)

class Organization(db.Model):
    """
    News organization model

    name Name of the organization
    description Description of the organization
    url Url to the organization's website
    logoUrl Url to the organization's logo
    articles List of articles belonging to this organization
    country Country this organization normally reports on
    """
    __tablename__ = 'organization'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    logoUrl = db.Column(db.String)

    articles = db.relationship('Article', back_populates='organization')
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country', back_populates='organizations')


    def __repr__(self):
        return '<Organization {0}>'.format(self.country)

class OrganizationSchemaNested(ma.Schema):
    #articles = fields.Nested('ArticleSchema', only='id')
    country = fields.Nested('CountrySchema', only=('id', 'name'))
    class Meta:
        fields = ('id', 'name', 'description', 'url', 'logoUrl', 'country')

class OrganizationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'url', 'logoUrl')

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

    organizations = db.relationship('Organization', back_populates='country')


    def __repr__(self):
        return '<Country {0}>'.format(self.name)

class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'capital', 'region', 'population', 'flagUrl')

class CountrySchemaNested(ma.Schema):
    organizations = fields.Nested(OrganizationSchema, many=True, only=('id', 'name'))
    class Meta:
        fields = ('id', 'name', 'capital', 'region', 'population', 'flagUrl', 'organizations')
