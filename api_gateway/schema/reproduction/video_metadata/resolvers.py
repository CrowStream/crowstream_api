""" video_metadata Resolvers"""

# Utilities
import graphene
import requests
import os

# Crowstream API Gateway
from .type_defs import UserVideoMetadata, UserVideoMetadataInput


REPRODUCTION_MS_URL = os.getenv('REPRODUCTION_MS_URL')
USER_MS_URL = os.getenv('USER_MS_URL')
#REPRODUCTION_MS_URL = "http://localhost:8080"


class Query(graphene.ObjectType):
    """Post query resolvers"""
    get_user_video_metadata_by_id = graphene.Field(UserVideoMetadata, user_id=graphene.String(name='user_id'), video_id=graphene.Int(name='video_id'))
    
    def resolve_get_user_video_metadata_by_id(parent, info, user_id, video_id):
        """Retrieve post by id resolver"""
        return requests.get('{0}/user-video-metadata/{1}/{2}'.format(REPRODUCTION_MS_URL, user_id, video_id)).json()


class CreateUserVideoMetadata(graphene.Mutation):
    """Create UserVideoMetadata Mutation"""

    user_video_metadata = graphene.Field(UserVideoMetadata, required=True)

    class Arguments:
        """Mutation Arguments"""
        user_video_metadata = UserVideoMetadataInput(required=True)
    
    @staticmethod
    def mutate(root, info, user_video_metadata=None):
        """Mutation"""
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get('{0}/whoAmI/'.format(USER_MS_URL), headers={'Authorization': token}).json()
        user_video_metadata['user_id'] = user_data['id']
        res = requests.post('{0}/user-video-metadata/'.format(REPRODUCTION_MS_URL), json=user_video_metadata).json()
        return CreateUserVideoMetadata(
            user_video_metadata=UserVideoMetadata(
                ID=res['ID']
            )
        )

class Mutation(graphene.ObjectType):
    """Class to compile all Mutations"""
    create_user_video_metadata = CreateUserVideoMetadata.Field()