from rest_framework import serializers
from .models import TeamMember

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

    def validate_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value

    def validate_email(self, value):
        # Exclude the current instance during updates
        if self.instance and self.instance.email == value:
            return value  # Allow the same email for the current instance
        if TeamMember.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value