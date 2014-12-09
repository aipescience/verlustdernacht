from rest_framework import viewsets
from lmdb.models import *
from lmdb.serializers import * 

class AnaBabelsbergViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaBabelsberg.objects.all()
    serializer_class = AnaBabelsbergSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaBbergSaveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaBbergSave.objects.all()
    serializer_class = AnaBbergSaveSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaDahlemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaDahlem.objects.all()
    serializer_class = AnaDahlemSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaDahlem2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaDahlem2.objects.all()
    serializer_class = AnaDahlem2Serializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaDahlem2OldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaDahlem2Old.objects.all()
    serializer_class = AnaDahlem2OldSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaDahlem4FilterlessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaDahlem4Filterless.objects.all()
    serializer_class = AnaDahlem4FilterlessSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaDahlem5RedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaDahlem5Red.objects.all()
    serializer_class = AnaDahlem5RedSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaDahlem6GreenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaDahlem6Green.objects.all()
    serializer_class = AnaDahlem6GreenSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaDahlem7BlueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaDahlem7Blue.objects.all()
    serializer_class = AnaDahlem7BlueSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaDahlemOldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaDahlemOld.objects.all()
    serializer_class = AnaDahlemOldSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaFreienbrinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaFreienbrink.objects.all()
    serializer_class = AnaFreienbrinkSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaFriedrichshagenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaFriedrichshagen.objects.all()
    serializer_class = AnaFriedrichshagenSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class AnaObservatorioDelTeideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnaObservatorioDelTeide.objects.all()
    serializer_class = AnaObservatorioDelTeideSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class MarkproBabelsberg2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarkproBabelsberg2.objects.all()
    serializer_class = MarkproBabelsberg2Serializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class MarkproBerlinFriedrichshainViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarkproBerlinFriedrichshain.objects.all()
    serializer_class = MarkproBerlinFriedrichshainSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class MarkproBerlinSpandauViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarkproBerlinSpandau.objects.all()
    serializer_class = MarkproBerlinSpandauSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class MarkproBerlinTreptowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MarkproBerlinTreptow.objects.all()
    serializer_class = MarkproBerlinTreptowSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class NutzungViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Nutzung.objects.all()
    serializer_class = NutzungSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SaveLocationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SaveLocations.objects.all()
    serializer_class = SaveLocationsSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmBabelsbergViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmBabelsberg.objects.all()
    serializer_class = SqmBabelsbergSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmBabelsberg3ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmBabelsberg3.objects.all()
    serializer_class = SqmBabelsberg3Serializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlem.objects.all()
    serializer_class = SqmDahlemSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlem2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlem2.objects.all()
    serializer_class = SqmDahlem2Serializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlem2OldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlem2Old.objects.all()
    serializer_class = SqmDahlem2OldSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlem2SaveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlem2Save.objects.all()
    serializer_class = SqmDahlem2SaveSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlem3ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlem3.objects.all()
    serializer_class = SqmDahlem3Serializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlem4FilterlessViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlem4Filterless.objects.all()
    serializer_class = SqmDahlem4FilterlessSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlem5RedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlem5Red.objects.all()
    serializer_class = SqmDahlem5RedSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlem6GreenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlem6Green.objects.all()
    serializer_class = SqmDahlem6GreenSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlem7BlueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlem7Blue.objects.all()
    serializer_class = SqmDahlem7BlueSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlemOldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlemOld.objects.all()
    serializer_class = SqmDahlemOldSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmDahlemSaveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmDahlemSave.objects.all()
    serializer_class = SqmDahlemSaveSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmFreienbrinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmFreienbrink.objects.all()
    serializer_class = SqmFreienbrinkSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmFriedrichshagenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmFriedrichshagen.objects.all()
    serializer_class = SqmFriedrichshagenSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmLocationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmLocations.objects.all()
    serializer_class = SqmLocationsSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmLocationsDevViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmLocationsDev.objects.all()
    serializer_class = SqmLocationsDevSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmLocationsDev2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmLocationsDev2.objects.all()
    serializer_class = SqmLocationsDev2Serializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmLocationsSave2ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmLocationsSave2.objects.all()
    serializer_class = SqmLocationsSave2Serializer
    paginate_by = 5
    paginate_by_param = 'page_size'

class SqmObservatorioDelTeideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SqmObservatorioDelTeide.objects.all()
    serializer_class = SqmObservatorioDelTeideSerializer
    paginate_by = 5
    paginate_by_param = 'page_size'

