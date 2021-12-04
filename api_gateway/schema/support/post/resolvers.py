""" Post Resovlers"""

# Utilities
import graphene
import requests

# Crowstream Api Gateway
from .type_defs import Post, Comment


class Query(graphene.ObjectType):
    retrieve_all_post = graphene.List(Post)
    retrieve_post_by_id = graphene.Field(Post, id_post=graphene.ID())
    
    def resolve_retrieve_all_post(parent, info):
        return requests.get('http://localhost:3000/posts').json()
    
    def resolve_retrieve_post_by_id(parent, info, id_post):
        return requests.get('http://{0}:{1}/posts/{2}'.format('localhost', '3000', id_post))