import graphene
import requests
import os

from .type_defs import Account, AccountCredentials, Token
from graphene_django import DjangoObjectType, DjangoListField

URL = "http://{}:{}".format(os.getenv("", "localhost"), os.getenv("", "3000"))

class SignIn(graphene.Mutation):
    class Arguments:
        accountCredentials = AccountCredentials()

    token = graphene.Field(lambda: Token)

    def mutate(root, info, accountCredentials):
        response = requests.post("{}/signin".format(URL), json=accountCredentials).json()
        return SignIn(
            Token(
                token=response['token']
            )
        )


class SignUp(graphene.Mutation):
    class Arguments:
        accountCredentials = AccountCredentials()

    account = graphene.Field(lambda: Account)

    def mutate(root, info, accountCredentials):
        newAccount = requests.post("{}/signup/".format(URL), json=accountCredentials).json()
        return SignUp(
            Account(
                id=newAccount['id'],
                email=newAccount['email'],
                is_email_verified=newAccount['is_email_verified']
            )
        )


class Mutations(graphene.ObjectType):
    signin = SignIn.Field()
    signup = SignUp.Field()


class Query(graphene.ObjectType):
    pass