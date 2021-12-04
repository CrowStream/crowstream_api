"""Support Request Type Defs"""

# Utilities
import graphene


class SupportResponseInput(graphene.InputObjectType):
    """Support Response GraphQL Input"""
    responder = graphene.NonNull(graphene.String)
    description = graphene.NonNull(graphene.String)
    files = graphene.List(graphene.String)


class SupportRequestInput(graphene.InputObjectType):
    """Support Request GraphQL Input"""
    user_id = graphene.NonNull(graphene.String)
    request_type = graphene.NonNull(graphene.String)
    description = graphene.NonNull(graphene.String)
    response = graphene.NonNull(SupportResponseInput)
    files = graphene.List(graphene.String)


class SupportResponse(graphene.ObjectType):
    """Support Response GraphQL Type"""
    _id = graphene.ID(name='_id')
    responder = graphene.NonNull(graphene.String, name='responder')
    description = graphene.NonNull(graphene.String, name='description')
    files = graphene.List(graphene.String, name='files')


class SupportRequest(graphene.ObjectType):
    """Support Request GraphQL Type"""
    _id = graphene.ID(name='_id')
    user_id = graphene.NonNull(graphene.String, name='user_id')
    request_type = graphene.NonNull(graphene.String, name='request_type')
    description = graphene.NonNull(graphene.String, name='description')
    response = graphene.NonNull(SupportResponse, name='response')
    files = graphene.List(graphene.String, name='files')
