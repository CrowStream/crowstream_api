import graphene

class likeVideoInput(graphene.InputObjectType):
    user_id = graphene.Field(graphene.String, name='user_id')
    video_id = graphene.NonNull(graphene.Int, name='video_id')
    like = graphene.NonNull(graphene.Int, name='like')

class likeVideo(graphene.ObjectType):
    user_id = graphene.NonNull(graphene.String, name='user_id')
    video_id = graphene.NonNull(graphene.Int, name='video_id')
    like = graphene.NonNull(graphene.Int, name='like')

