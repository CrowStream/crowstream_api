import graphene
import requests

from .type_defs import Account, AccountCredentials, Token
from ..server import URL


class Query(graphene.ObjectType):
    who_am_i = graphene.NonNull(Account)

    def resolve_who_am_i(parent, info):
        token = info.context.META.get('HTTP_AUTHORIZATION')
        return requests.get("{}/whoAmI".format(URL), headers={'Authorization': token}).json()


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


class Mutation(graphene.ObjectType):
    signin = SignIn.Field()
    signup = SignUp.Field()
