"""reproduction Type Defs"""

# Utilities
import graphene

class UserVideoMetadata(graphene.ObjectType):
    ID = graphene.ID(name='ID')
    user_id = graphene.String(name='user_id')
    video_id = graphene.Int(name='video_id')
    video_progress = graphene.Float(name='video_progress')
    video_progress_time = graphene.String(name='video_progress_time')

class UserVideoMetadataInput(graphene.InputObjectType):
    user_id = graphene.String(name='user_id')
    video_id = graphene.Int(name='video_id')
    video_progress = graphene.Float(name='video_progress')
    video_progress_time = graphene.String(name='video_progress_time')