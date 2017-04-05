from unittest import main, TestCase
from models import Organization, Article, Country
from app import create_app, db

ctx = create_app()
ctx.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
ctx.app_context().push()


class Tests(TestCase):
    def setUp(self):
        db.session.query(Country).delete()
        db.session.query(Article).delete()
        db.session.query(Organization).delete()
        db.session.commit()
        db.drop_all()
        db.create_all()

    def test_organization_1(self):
        s = Organization(name='Organization1')
        self.assertEqual(s.name, 'Organization1')

    def test_organization_2(self):
        s = Organization(name='Organization1')
        db.session.add(s)
        self.assertEqual(len(Organization.query.all()), 1)

    def test_organization_3(self):
        s = Organization(name='Organization1')
        db.session.add(s)
        first = Organization.query.first()
        self.assertEqual(first.name, 'Organization1')

    def test_organization_4(self):
        c = Country(name='USA')
        s = Organization(name='Organization1', country=c)
        db.session.add(s)
        first = Organization.query.first()
        self.assertEqual(first.country.name, 'USA')

    def test_organization_5(self):
        a = Article(title='Breaking: Milking Postponed Until Saturday')
        s = Organization(name='CowNews')
        s.articles.append(a)
        db.session.add(s)
        first = Organization.query.first()
        self.assertEqual(len(first.articles), 1)

    def test_article_1(self):
        a = Article(title='Article1')
        self.assertEqual(a.title, 'Article1')

    def test_article_2(self):
        a = Article(title='Article1')
        db.session.add(a)
        self.assertEqual(len(Article.query.all()), 1)

    def test_article_3(self):
        a = Article(title='Article1')
        db.session.add(a)
        first = Article.query.first()
        self.assertEqual(first.title, 'Article1')

    def test_article_4(self):
        s = Organization(name='CowNews')
        a = Article(title='Why you shouldn\'t drink your own milk', organization=s)
        db.session.add(a)
        first = Article.query.first()
        self.assertEqual(first.organization.name, 'CowNews')

    def test_article_5(self):
        c = Country(name='Cowland')
        a = Article(title='Why you shouldn\'t drink your own milk')
        a.countries.append(c)
        db.session.add(a)
        first = Article.query.first()
        self.assertEqual(len(first.countries), 1)
        self.assertEqual(len(c.articles), 1)

    def test_country_1(self):
        c = Country(name='Country1')
        self.assertEqual(c.name, 'Country1')

    def test_country_2(self):
        c = Country(name='Country1')
        db.session.add(c)
        self.assertEqual(len(Country.query.all()), 1)

    def test_country_3(self):
        c = Country(name='Country1')
        db.session.add(c)
        first = Country.query.first()
        self.assertEqual(first.name, 'Country1')

    def test_country_4(self):
        c = Country(name='Cowland')
        a = Article(title='President Cowy McMoo to Ban Strawberry Milk')
        c.articles.append(a)
        db.session.add(c)
        first = Country.query.first()
        self.assertEqual(len(first.articles), 1)

    def test_country_5(self):
        c = Country(name='Cowland')
        s = Organization(name='Monthly Milkpost')
        c.organizations.append(s)
        db.session.add(s)
        first = Country.query.first()
        self.assertEqual(len(first.organizations), 1)

if __name__ == "__main__":
    main()
