"""reproduction Type Defs"""

# Utilities
import graphene

class ClickCountMetadata(graphene.ObjectType):
    ID = graphene.ID(name='ID')
    user_id = graphene.String(name='user_id')
    video_id = graphene.Int(name='video_id')
    click_description = graphene.Boolean(name='click_description')
    click_video = graphene.Boolean(name='click_video')

class ClickCountMetadataInput(graphene.InputObjectType):
    user_id = graphene.String(name='user_id')
    video_id = graphene.Int(name='video_id')
    click_description = graphene.Boolean(name='click_description')
    click_video = graphene.Boolean(name='click_video')