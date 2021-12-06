import graphene

class Account(graphene.ObjectType):
    id = graphene.NonNull(graphene.String, name='id')
    email = graphene.NonNull(graphene.String, name='email')
    is_email_verified = graphene.Boolean(name='is_email_verified')


class Token(graphene.ObjectType):
    token = graphene.NonNull(graphene.String, name='token')
    refreshToken = graphene.String(name='refreshToken')


class AccountCredentials(graphene.InputObjectType):
    email = graphene.NonNull(graphene.String, name='email')
    password = graphene.NonNull(graphene.String, name='password')