from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):

	#python manage.py shell
	#from sp_api.serializers import NoteSerializer
	#serializer = NoteSerializer()
	#print(repr(serializer))

    class Meta:
        model = Note
        fields = ('__all__')