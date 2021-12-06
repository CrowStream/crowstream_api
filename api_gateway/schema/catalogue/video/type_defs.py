import graphene


class Video(graphene.ObjectType):
    id = graphene.NonNull(graphene.Int, name='id')
    description = graphene.NonNull(graphene.String, name="description")
    video_name = graphene.NonNull(graphene.String, name="video_name")
    release_year = graphene.NonNull(graphene.Int, name="release_year")
    #producer = graphene.String(name="producer")
    #irector = graphene.String(name="director")
    #genre = graphene.NonNull(graphene.String, name="genre")