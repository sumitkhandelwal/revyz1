from rest_framework import serializers
from JobPortal.models import Candidates

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields = '__all__'