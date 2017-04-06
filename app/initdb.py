from app import create_app
from models import Country, Article, Organization
import pickle

with create_app().app_context():

    data = pickle.load( open("stores/data/data.pickle", "rb"))
    org_id = {}

    for o in data['organizations']:
        org_id[o['id']] = o['name']

    from models import db

    Article.__table__.drop()
    db.create_all()

    for ar in data['articles']:
        print("for loop start" + "\n")
        org = Organization.query.filter_by(name = org_id[ar['organization']['id']]).first()
        print(str(org.id))

        article = Article(title = ar['title'], author = ar['author'], description = ar['description'], publishDate = ar['publishedAt'], url = ar['url'], imageUrl = ar['urlToImage'], organization_id = org.id) #, countries = ar['countries'])
        print(str(article))

        db.session.add(article)
        print("added")
    db.session.commit()
    print("commited")

    print(str(Organization.query.all()))
    print(str(Article.querty.all()))





















'''
    #organizations
    for org in data['organizations']:
        #print(str(org) + "\n")
        organization = Organization(name = org['name'], description = org['description'], url = org['url'], logoUrl = org['urlsToLogos']['medium'], country_id = org['country']['id'])
        db.session.add(organization)

    db.session.commit()

    #countries
    id_countries = {}
    for x in data['countries']:
        id_countries[x['id']]  = x['name']


    from models import db
    db.create_all()
    for org in data['organizations']:
        country = Country.query.filter_by(name = id_countries[org['country']['id']]).first()
        organization = Organization(name = org['name'], description = org['description'], url = org['url'], logoUrl = org['urlsToLogos']['medium'], country_id = country.id)
        db.session.add(organization)

    db.session.commit()

    print(str(Organization.query.all()))



'''
