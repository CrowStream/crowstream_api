"""Post Type Defs"""

# Utilities
import graphene


class CommentInput(graphene.InputObjectType):
    """Comment GraphQL Input"""
    user_id = graphene.NonNull(graphene.String, name='user_id')
    user_nick = graphene.String(name='user_nick')
    description = graphene.NonNull(graphene.String, name='description')
    files = graphene.List(graphene.String, name='files')


class PostInput(graphene.InputObjectType):
    """Post GraphQL Input"""
    user_id = graphene.NonNull(graphene.String, name='user_id')
    user_nick = graphene.String(name='user_nick')
    title = graphene.NonNull(graphene.String, name='title')
    description = graphene.NonNull(graphene.String, name='description')
    comments = graphene.List(CommentInput, name='comments')
    files = graphene.List(graphene.String, name='files')
    

class Comment(graphene.ObjectType):
    """Comment GraphQL Type"""
    _id = graphene.NonNull(graphene.ID, name='_id')
    user_id = graphene.NonNull(graphene.String, name='user_id')
    user_nick = graphene.String(name='user_nick')
    description = graphene.NonNull(graphene.String, name='description')
    files = graphene.List(graphene.String, name='files')


class Post(graphene.ObjectType):
    """Post GraphQL Type"""
    _id = graphene.NonNull(graphene.ID, name='_id')
    user_id = graphene.NonNull(graphene.String, name='user_id')
    user_nick = graphene.String(name='user_nick')
    title = graphene.NonNull(graphene.String, name='title')
    description = graphene.NonNull(graphene.String, name='description')
    comments = graphene.List(Comment, name='comments')
    files = graphene.List(graphene.String, name='files')

    