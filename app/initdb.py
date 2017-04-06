from app import create_app
from models import Country, Article, Organization
import pickle

with create_app().app_context():

    data = pickle.load(open("stores/data/data.pickle", "rb"))

    from models import db
    db.create_all()

    # Counry article relation
    id_countries = {}
    for x in data['countries']:
        id_countries[x['id']] = x['name']
    # print(id_countries)

    # For loop the articles
    for art in data['articles']:
        #print(str(art) + "\n")
        # get the article query
        a = Article.query.filter_by(title=art['title']).first()
        for cou in art['countries']:
            # get country
            # print(cou)
            c_name = id_countries[cou['id']]
            # print(c_name)
            c = Country.query.filter_by(name=c_name).first()
            a.countries.append(c)
        print(a.countries)
    db.session.commit()

'''

    from models import db
    db.create_all()


    for ar in data['articles']:
        #print("for loop start" + "\n")
        org = Organization.query.filter_by(name = org_id[ar['organization']['id']]).first()
        #print(str(org.id))
    
        article = Article(title = ar['title'], author = ar['author'], description = ar['description'], publishDate = ar['publishedAt'], url = ar['url'], imageUrl = ar['urlToImage'], organization_id = org.id) #, countries = ar['countries'])
        print(str(article))
        
        db.session.add(article)
        #print("added")
    db.session.commit()
    #print("commited")




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

    #Organizations
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

    for c in data['countries']:
        country = Country(name = c['name'], capital = c['capital'], region = c['region'], population = c['population'], flagUrl = c['flag'])
        print(country)
        db.session.add(country)
        
    db.session.commit()

    print(str(Country.query.all()))


'''
