import graphene
import requests

from .type_defs import Profile, ProfileInput, Profiles
from ..server import URL

class Query(graphene.ObjectType):
    profiles_by_id = graphene.NonNull(Profile, profile_id=graphene.String(name='id'))
    user_profiles = graphene.NonNull(Profiles)

    def resolve_profiles_by_id(parent, info, profile_id):
        token = info.context.META.get('HTTP_AUTHORIZATION')
        return requests.get("{}/profiles/{}".format(URL, profile_id), headers={'Authorization': token}).json()

    def resolve_user_profiles(parent, info):
        token = info.context.META.get('HTTP_AUTHORIZATION')
        return requests.get("{}/profiles".format(URL), headers={'Authorization': token}).json()


class CreateProfile(graphene.Mutation):
    class Arguments:
        newProfile = ProfileInput()

    profile = graphene.Field(lambda: Profile)

    def mutate(root, info, newProfile):
        token = info.context.META.get('HTTP_AUTHORIZATION')
        response = requests.post(
            "{}/profiles/".format(URL),
            headers={'Authorization': token},
            json=newProfile
        ).json()
        return CreateProfile(
            Profile(
                id=response['id'],
                account_id=response['account_id'],
                name=response['name']
            )
        )


class Mutation(graphene.ObjectType):
    create_profile = CreateProfile.Field()
