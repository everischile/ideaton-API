from rest_framework import serializers
from rest_framework.serializers import CreateOnlyDefault
from rest_framework.serializers import CurrentUserDefault
from api.models import Idea, Vote, User
from api.models import Commentary, Image
from drf_extra_fields.fields import Base64ImageField


class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class GetIdIdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = ('id',)


class GetVoteSerializer(serializers.ModelSerializer):
    user = GetUserSerializer()
    idea = GetIdIdeaSerializer()

    class Meta:
        model = Vote
        fields = ('user', 'idea')


class GetCommentarySerializer(serializers.ModelSerializer):
    user = GetUserSerializer()
    idea = GetIdIdeaSerializer()

    class Meta:
        model = Commentary
        fields = ('idea', 'user.username', 'commentary')


class GetImageSerializer(serializers.ModelSerializer):
    idea = GetIdIdeaSerializer()

    class Meta:
        model = Image
        fields = ('idea', 'image')


class GetIdeaSerializer(serializers.ModelSerializer):
    user = GetUserSerializer()

    class Meta:
        model = Idea
        fields = ('id', 'title', 'description', 'url_video',
                  'cant_vote', 'category', 'main_image', 'user.username')


class PostIdeaSerializer(serializers.ModelSerializer):
    main_image = Base64ImageField(required=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=CreateOnlyDefault(CurrentUserDefault()),
    )

    class Meta:
        model = Idea
        fields = ('title', 'description', 'url_video', 'main_image', 'user')


class PostCommentarySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=CreateOnlyDefault(CurrentUserDefault()),
    )
    idea = serializers.PrimaryKeyRelatedField(
        queryset=Idea.objects.all(),
    )

    class Meta:
        model = Commentary
        fields = ('idea', 'user', 'commentary')


class PostVoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=CreateOnlyDefault(CurrentUserDefault()),
    )
    idea = serializers.PrimaryKeyRelatedField(
        queryset=Idea.objects.all(),
    )

    class Meta:
        model = Vote
        fields = ('idea', 'user')
