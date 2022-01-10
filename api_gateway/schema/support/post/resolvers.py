""" Post Resovlers"""

# Utilities
import graphene
import requests
import os

# Crowstream API Gateway
from .type_defs import Comment, CommentInput, Post, PostInput


SUPPORT_MS_URL = os.getenv('SUPPORT_MS_URL')
USER_MS_URL = os.getenv('USER_MS_URL')


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
        post = PostInput(required=True)
    
    @staticmethod
    def mutate(root, info, post=None):
        """Mutation"""
        print(USER_MS_URL)
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get('{0}/whoAmI/'.format(USER_MS_URL), headers={'Authorization': token}).json()
        post['user_id'] = user_data['id']
        res = requests.post('{0}/posts/'.format(SUPPORT_MS_URL), json=post).json()
        return CreatePost(
            post=Post(
                _id=res['_id'],
                user_id=res['user_id'],
                description=res['description'],
                comments=res['comments'],
                files=res['files']
            )
        )


class CreateComment(graphene.Mutation):
    """Create Comment Mutation"""
    
    comment = graphene.Field(Comment, required=True)
    
    class Arguments:
        """Mutation Arguments"""
        id_post = graphene.ID(required=True, name='id_post')
        comment = CommentInput(required=True, name='comment')

    @staticmethod
    def mutate(root, info, id_post=None, comment=None):
        """Mutation"""
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get('{0}/whoAmI/'.format(USER_MS_URL), headers={'Authorization': token}).json()
        comment['user_id'] = user_data['id']
        comment['email'] = user_data['email']
        res = requests.post('{0}/posts/{1}/comments'.format(SUPPORT_MS_URL, id_post), json=comment).json()
        return CreateComment(
            comment=Comment(
                _id=res['_id'],
                user_id=res['user_id'],
                description=res['description'],
                files=res['files']
            )
        )
        

class UpdatePost(graphene.Mutation):
    """Update Post Mutation"""

    post = graphene.Field(Post, required=True)

    class Arguments:
        """Mutation Arguments"""
        id_post = graphene.ID(required=True, name='id_post')
        post =PostInput(required=True, name='post')

    @staticmethod
    def mutate(root, info, id_post=None, post=None):
        """Mutation"""
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get('{0}/whoAmI/'.format(USER_MS_URL), headers={'Authorization': token}).json()
        post['user_id'] = user_data['id']
        res = requests.put('{0}/posts/{1}/'.format(SUPPORT_MS_URL, id_post), json=post).json()
        return UpdatePost(
            post=Post(
                _id=res['_id'],
                user_id=res['user_id'],
                description=res['description'],
                comments=res['comments'],
                files=res['files']
            )
        )


class DeletePost(graphene.Mutation):
    """Delete Post Mutation"""

    boolean = graphene.Field(graphene.Boolean)

    class Arguments:  
        """Mutation Arguments"""
        id_post = graphene.ID(required=True, name='id_post')

    @staticmethod
    def mutate(root, info, id_post=None):
        """Mutation"""
        requests.delete('{0}/posts/{1}/'.format(SUPPORT_MS_URL, id_post))
        return DeletePost(boolean=None)


class Mutation(graphene.ObjectType):
    """Class to compile all Mutations"""
    create_post = CreatePost.Field()
    create_comment = CreateComment.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()