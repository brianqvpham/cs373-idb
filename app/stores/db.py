from models import Organization, OrganizationSchema, OrganizationSchemaNested, Country, CountrySchema, CountrySchemaNested

class DBStore():
    def get(self, Model, Schema, id, **args):
        if(id):
            resource = Model.query.get(id)
            schema = Schema()
        else:
            resource = Model.query.all()
            schema = Schema(many=True)
        return schema.dump(resource).data

class OrganizationStore(DBStore):
    def get(self, id=None, **args):
        if(id):
            schema = OrganizationSchemaNested
        else:
            schema = OrganizationSchema
        return super().get(Organization, schema, id, **args)

class CountryStore(DBStore):
    def get(self, id=None, **args):
        if(id):
            schema = CountrySchemaNested
        else:
            schema = CountrySchema
        return super().get(Country, schema, id, **args)

