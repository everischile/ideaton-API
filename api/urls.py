from django.conf.urls import include, url
from api.views import IdeaViewSet, VoteViewSet, PostCommentaryViewSet
from api.views import CommentaryViewSet, ImageViewSet, PostIdeaViewSet, PostVoteViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token


router = SimpleRouter()
router.register(r'ideas', IdeaViewSet)
router.register(r'votos', VoteViewSet)
router.register(r'comentarios', CommentaryViewSet)
router.register(r'imagenes', ImageViewSet)
router.register(r'upload_idea', PostIdeaViewSet)
router.register(r'insert_comentario', PostCommentaryViewSet)
router.register(r'insert_voto', PostVoteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api/login/', include('rest_social_auth.urls_session')),
    url(r'^api/login/', include('rest_social_auth.urls_token')),
    url(r'^api/login/', include('rest_social_auth.urls_jwt')),
    url(r'^api-token-auth/', obtain_jwt_token),
]
