from rest_framework.routers import SimpleRouter

from .views import CursoViewSet, AvaliacaoViewSet


router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
