"""Post Type Defs"""

# Utilities
import graphene


class CommentInput(graphene.InputObjectType):
    """Comment GraphQL Input"""
    user_id = graphene.NonNull(graphene.String)
    description = graphene.NonNull(graphene.String)
    files = graphene.List(graphene.String)


class PostInput(graphene.InputObjectType):
    """Post GraphQL Input"""
    user_id = graphene.Field(graphene.String)
    description = graphene.NonNull(graphene.String)
    comments = graphene.List(CommentInput)
    files = graphene.List(graphene.String)
    

class Comment(graphene.ObjectType):
    """Comment GraphQL Type"""
    _id = graphene.ID(name='_id')
    user_id = graphene.String(name='user_id')
    description = graphene.String(name='description')
    files = graphene.List(graphene.String, name='files')


class Post(graphene.ObjectType):
    """Post GraphQL Type"""
    _id = graphene.ID(name='_id')
    user_id = graphene.NonNull(graphene.String, name='user_id')
    description = graphene.NonNull(graphene.String, name='description')
    comments = graphene.List(Comment, name='comments')
    files = graphene.List(graphene.String, name='files')

    