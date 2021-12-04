import graphene

from graphene_django import DjangoObjectType, DjangoListField

class Account(graphene.ObjectType):
    id = graphene.NonNull(graphene.String, name='id')
    email = graphene.NonNull(graphene.String, name='email')
    is_email_verified = graphene.Boolean


class Token(graphene.ObjectType):
    token = graphene.NonNull(graphene.String, name='token')


class AccountCredentials(graphene.InputObjectType):
    email = graphene.NonNull(graphene.String, name='email')
    password = graphene.NonNull(graphene.String, name='password')