import graphene
import requests

from graphene_django import DjangoObjectType, DjangoListField


# --------------------USER_MS--------------------

## Account schemas

class Account(graphene.ObjectType):
    id = graphene.NonNull(graphene.String)
    email = graphene.NonNull(graphene.String)
    is_email_verified = graphene.Boolean


class Token(graphene.ObjectType):
    token = graphene.NonNull(graphene.String)


class AccountCredentials(graphene.InputObjectType):
    email = graphene.NonNull(graphene.String)
    password = graphene.NonNull(graphene.String)


## Profile schemas

class Profile(graphene.ObjectType):
    id = graphene.NonNull(graphene.String)
    account_id = graphene.String
    name = graphene.NonNull(graphene.String)


class ProfileInput(graphene.InputObjectType):
    name = graphene.NonNull(graphene.String)


class Profiles(graphene.ObjectType):
    account_id = graphene.NonNull(graphene.String)
    profiles = graphene.NonNull(graphene.List(Profile))



# --------------------SUPPORT_MS Schemas--------------------


class CommentInput(graphene.InputObjectType):
    user_id = graphene.NonNull(graphene.String)
    description = graphene.NonNull(graphene.String)
    files = graphene.List(graphene.String)
    email = graphene.String()


class PostInput(graphene.InputObjectType):
    user_id = graphene.NonNull(graphene.String)
    description = graphene.NonNull(graphene.String)
    comments = graphene.List(CommentInput)
    files = graphene.List(graphene.String)
    

class Comment(graphene.ObjectType):
    _id = graphene.ID(name='_id')
    user_id = graphene.String(name='user_id')
    description = graphene.String(name='description')
    files = graphene.List(graphene.String, name='files')


class Post(graphene.ObjectType):
    _id = graphene.ID(name='_id')
    user_id = graphene.NonNull(graphene.String, name='user_id')
    description = graphene.NonNull(graphene.String, name='description')
    comments = graphene.List(Comment, name='comments')
    files = graphene.List(graphene.String, name='files')



class Query(graphene.ObjectType):
    # SUPPORT_MS
    retrieve_all_post = graphene.List(Post)
    retrieve_post_by_id = graphene.Field(Post, id_post=graphene.ID())

    # SUPPORT_MS
    def resolve_retrieve_all_post(parent, info):
        print()
        print("Parent: {}".format(parent))
        print("Into: {}".format(info))
        print(requests.get('http://localhost:3000/posts').json())
        print()
        return requests.get('http://localhost:3000/posts').json()
        
    
    def resolve_retrieve_post_by_id(parent, info, id_post):
        print("Parent: {}".format(parent))
        print("Into: {}".format(info))
        print("id_post: {}".format(id_post))
        return requests.get('http://{0}:{1}/posts/{2}'.format('localhost', '3000', id_post))
        
        



schema = graphene.Schema(query=Query)


