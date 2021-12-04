import graphene
import requests
import os

from .type_defs import Account, AccountCredentials, Token
from graphene_django import DjangoObjectType, DjangoListField

URL = "{}:{}".format(os.getenv("", "localhost"), os.getenv("", "3000"))

class SignIn(graphene.Mutation):
    class Arguments:
        accountCredentials = AccountCredentials()

    token = Token()

    def mutate(root, info, accountCredentials):
        token = requests.post("{}/signin/".format(URL), accountCredentials).json()
        return token


class SignUp(graphene.Mutation):
    class Arguments:
        accountCredentials = AccountCredentials()

    account = Account()

    def mutate(root, info, accountCredentials):
        account = requests.post("{}/signup/".format(URL), accountCredentials).json()
        return account


class Mutations(graphene.ObjectType):
    signin = SignIn.Field()
    signup = SignUp.Field()


class Query(graphene.ObjectType):
    pass