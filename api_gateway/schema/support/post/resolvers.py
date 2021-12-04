""" Post Resovlers"""

# Utilities
import graphene
import requests
import os

# Crowstream Api Gateway
from .type_defs import Post


SUPPORT_MS_URL = 'http://{0}:{1}'.format(os.getenv('SUPPORT_MS_HOST'), os.getenv('SUPPORT_MS_PORT'))

class Query(graphene.ObjectType):
    """Post query resolvers"""
    retrieve_all_post = graphene.NonNull(graphene.List(Post))
    retrieve_post_by_id = graphene.Field(Post, id_post=graphene.ID(name='id_post'))
    
    def resolve_retrieve_all_post(parent, info):
        """Retrieve all post resolver"""
        return requests.get('{0}/posts/'.format(SUPPORT_MS_URL)).json()
    
    def resolve_retrieve_post_by_id(parent, info, id_post):
        """Retrieve post by id resolver"""
        return requests.get('{0}/posts/{1}/'.format(SUPPORT_MS_URL, id_post)).json()