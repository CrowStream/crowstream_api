import graphene


class Video(graphene.ObjectType):
    id = graphene.NonNull(graphene.Int, name='id')
    description = graphene.NonNull(graphene.String, name="description")
    video_name = graphene.NonNull(graphene.String, name="video_name")
    release_year = graphene.NonNull(graphene.Int, name="release_year")
    thumbnail_url = graphene.NonNull(graphene.String, name="thumbnail_url")
    video_url = graphene.NonNull(graphene.String, name="video_url")
    producer = graphene.String(name="producer")
    director = graphene.String(name="director")
    genre = graphene.String(name="genre")