""" click_metadata Resolvers"""

# Utilities
import graphene
import requests
import os

# Crowstream API Gateway
from .type_defs import ClickCountMetadata, ClickCountMetadataInput


REPRODUCTION_MS_URL = os.getenv('REPRODUCTION_MS_URL')
USER_MS_URL = os.getenv('USER_MS_URL')
#REPRODUCTION_MS_URL = "http://localhost:8080"


class Query(graphene.ObjectType):
    """Post query resolvers"""
    get_click_count_metadata_by_id = graphene.Field(ClickCountMetadata, user_id=graphene.String(name='user_id'), video_id=graphene.Int(name='video_id'))
    get_all_click_count_metadata = graphene.NonNull(graphene.List(ClickCountMetadata))
    
    def resolve_get_click_count_metadata_by_id(parent, info, user_id, video_id):
        """Retrieve post by id resolver"""
        return requests.get('{0}/click-count-metadata/{1}/{2}'.format(REPRODUCTION_MS_URL, user_id, video_id)).json()

    def resolve_get_all_click_count_metadata(parent, info):
        """Retrieve all click count metadata resolver"""
        return requests.get('{0}/click-count-metadata/'.format(REPRODUCTION_MS_URL)).json()


class CreateClickCountMetadata(graphene.Mutation):
    """Create UserVideoMetadata Mutation"""

    click_count_metadata = graphene.Field(ClickCountMetadata, required=True)

    class Arguments:
        """Mutation Arguments"""
        click_count_metadata = ClickCountMetadataInput(required=True)
    
    @staticmethod
    def mutate(root, info, click_count_metadata=None):
        """Mutation"""
        #token = info.context.META.get('HTTP_AUTHORIZATION')
        #user_data = requests.get('{0}/whoAmI/'.format(USER_MS_URL), headers={'Authorization': token}).json()
        #click_count_metadata['user_id'] = user_data['id']
        res = requests.post('{0}/click-count-metadata/'.format(REPRODUCTION_MS_URL), json=click_count_metadata).json()
        return CreateClickCountMetadata(
            click_count_metadata=ClickCountMetadata(
                ID=res['ID'],
            )
        )

class UpdateClickCountMetadata(graphene.Mutation):
    """Update UserVideoMetadata Mutation"""

    click_count_metadata = graphene.Field(ClickCountMetadata, required=True)

    class Arguments:
        """Mutation Arguments"""
        click_count_metadata = ClickCountMetadataInput(required=True)
    
    @staticmethod
    def mutate(root, info, click_count_metadata=None):
        """Mutation"""
        #token = info.context.META.get('HTTP_AUTHORIZATION')
        #user_data = requests.get('{0}/whoAmI/'.format(USER_MS_URL), headers={'Authorization': token}).json()
        #click_count_metadata['user_id'] = user_data['id']
        res = requests.put('{0}/click-count-metadata/'.format(REPRODUCTION_MS_URL), json=click_count_metadata).json()
        return CreateClickCountMetadata(
            click_count_metadata=ClickCountMetadata(
                ID=res['ID'],
                user_id=res['user_id'],
                video_id=res['video_id'],
                click_description=res['click_description'],
                click_video=res['click_video'],
            )
        )

class Mutation(graphene.ObjectType):
    """Class to compile all Mutations"""
    create_click_count_metadata = CreateClickCountMetadata.Field()
    update_click_count_metadata = UpdateClickCountMetadata.Field()