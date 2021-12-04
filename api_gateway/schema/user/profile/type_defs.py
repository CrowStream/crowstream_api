import graphene

class Profile(graphene.ObjectType):
    id = graphene.NonNull(graphene.String, name='id')
    account_id = graphene.String(name='account_id')
    name = graphene.NonNull(graphene.String, name='name')

class ProfileInput(graphene.InputObjectType):
    name = graphene.NonNull(graphene.String, name='name')

class Profile(graphene.ObjectType):
    account_id = graphene.NonNull(String, name='account_id')
    profiles = graphene.List(Profile, name='profile')