""" Post Resovlers"""

# Utilities
import graphene
import requests
import os

# Crowstream API Gateway
from .type_defs import Comment, CommentInput, Post, PostInput


SUPPORT_MS_URL = 'http://{0}:{1}'.format(os.getenv('SUPPORT_MS_HOST'), os.getenv('SUPPORT_MS_PORT'))
USER_MS_URL = 'http://{0}:{1}'.format(os.getenv('USER_MS_HOST'), os.getenv('USER_MS_PORT'))

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


class CreatePost(graphene.Mutation):
    """Create Post Mutation"""

    post = graphene.Field(Post, required=True)

    class Arguments:
        """Mutation Arguments"""
        post = graphene.Field(PostInput, required=True)
    
    @staticmethod
    def mutate(root, info, post=None):
        """Mutation"""
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get('{0}/whoAmI/'.format(SUPPORT_MS_URL), headers={'Authorization': token}).json()
        post.user_id = user_data.id
        res = requests.post('{0}/posts/'.format(SUPPORT_MS_URL), data=post).json()
        return CreatePost(post=Post(res))


class CreateComment(graphene.Mutation):
    """Create Comment Mutation"""
    
    comment = graphene.Field(Comment, required=True)
    
    class Arguments:
        """Mutation Arguments"""
        id_post = graphene.Field(graphene.ID, required=True)
        comment = graphene.Field(CommentInput, required=True)

    @staticmethod
    def mutate(root, info, comment=None):
        """Mutation"""
        pass


class UpdatePost(graphene.Mutation):
    """Update Post Mutation"""

    post = graphene.Field(Post, required=True)

    class Arguments:
        """Mutation Arguments"""
        id_post = graphene.Field(graphene.ID, required=True)
        post = graphene.Field(PostInput, required=True)

    @staticmethod
    def mutate(root, info, post=None):
        """Mutation"""
        pass


class DeletePost(graphene.Mutation):
    """Delete Post Mutation"""

    boolean = graphene.Field(graphene.Boolean)

    class Arguments:  
        """Mutation Arguments"""
        id_post = graphene.Field(graphene.ID, required=True)

    @staticmethod
    def mutate(root, info, boolean=None):
        """Mutation"""
        pass


class Mutation(graphene.ObjectType):
    """Class to compile all Mutations"""
    create_post = CreatePost.Field()
    create_comment = CreateComment.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()