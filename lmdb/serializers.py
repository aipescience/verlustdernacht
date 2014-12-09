from rest_framework import serializers
from lmdb.models import * 

class AnaBabelsbergSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaBabelsberg 

class AnaBbergSaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaBbergSave 

class AnaDahlemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaDahlem 

class AnaDahlem2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaDahlem2 

class AnaDahlem2OldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaDahlem2Old 

class AnaDahlem4FilterlessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaDahlem4Filterless 

class AnaDahlem5RedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaDahlem5Red 

class AnaDahlem6GreenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaDahlem6Green 

class AnaDahlem7BlueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaDahlem7Blue 

class AnaDahlemOldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaDahlemOld 

class AnaFreienbrinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaFreienbrink 

class AnaFriedrichshagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaFriedrichshagen 

class AnaObservatorioDelTeideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaObservatorioDelTeide 

class MarkproBabelsberg2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarkproBabelsberg2 

class MarkproBerlinFriedrichshainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarkproBerlinFriedrichshain 

class MarkproBerlinSpandauSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarkproBerlinSpandau 

class MarkproBerlinTreptowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarkproBerlinTreptow 

class NutzungSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nutzung 

class SaveLocationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SaveLocations 

class SqmBabelsbergSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmBabelsberg 

class SqmBabelsberg3Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmBabelsberg3 

class SqmDahlemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlem 

class SqmDahlem2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlem2 

class SqmDahlem2OldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlem2Old 

class SqmDahlem2SaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlem2Save 

class SqmDahlem3Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlem3 

class SqmDahlem4FilterlessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlem4Filterless 

class SqmDahlem5RedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlem5Red 

class SqmDahlem6GreenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlem6Green 

class SqmDahlem7BlueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlem7Blue 

class SqmDahlemOldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlemOld 

class SqmDahlemSaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmDahlemSave 

class SqmFreienbrinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmFreienbrink 

class SqmFriedrichshagenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmFriedrichshagen 

class SqmLocationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmLocations 

class SqmLocationsDevSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmLocationsDev 

class SqmLocationsDev2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmLocationsDev2 

class SqmLocationsSave2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmLocationsSave2 

class SqmObservatorioDelTeideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SqmObservatorioDelTeide 
