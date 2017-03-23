from unittest import main, TestCase
from models import Source, Article, Country
from app import create_app, db

ctx = create_app()
ctx.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
ctx.app_context().push()
db.create_all()

class Tests(TestCase):
    def test_source_1(self):
        s = Source(name='Source1')
        self.assertEqual(s.name, 'Source1')

    def test_source_2(self):
        s = Source(name='Source1')
        db.session.add(s)
        self.assertEqual(len(Source.query.all()), 1)

    def test_source_3(self):
        s = Source(name='Source1')
        db.session.add(s)
        first = Source.query.first()
        self.assertEqual(first.name, 'Source1')

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

if __name__ == "__main__":
    main()
