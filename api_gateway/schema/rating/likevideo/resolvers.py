# Utilities
import graphene
import requests
import os

# Crowstream API Gateway
from .type_defs import likeVideo, likeVideoInput

RATING_MS_URL = os.getenv('RATING_MS_URL')
USER_MS_URL = os.getenv('USER_MS_URL')

class Liking(graphene.Mutation):
    """Create Post Mutation"""

    liked = graphene.Field(likeVideo, required=True)

    class Arguments:
        """Mutation Arguments"""
        liked = likeVideoInput(required=True)
    
    @staticmethod
    def mutate(root, info, liked=None):
        #token = info.context.META.get('HTTP_AUTHORIZATION')
        #user_data = requests.get('{0}/whoAmI/'.format(USER_MS_URL), headers={'Authorization': token}).json()
        #liked['user_id'] = user_data['id']
        res = requests.post('{0}/likevideo/'.format(RATING_MS_URL), json=liked).json()
        return Liking(
            liked=likeVideo(
                user_id=res['id']['user_id'],
                video_id=res['id']['video_id'],
                like=res['like']
            )
        )

class Mutation(graphene.ObjectType):
    """Class to compile all Mutations"""
    liking = Liking.Field()