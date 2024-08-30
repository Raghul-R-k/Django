from rest_framework import serializers
from .models import Author

 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','city','age']
        read_only_fields = ['id']

    #add custom validator 
    # def validate(self,data):
    #     if len(data['name'] == 0):
    #         raise serializers.ValidationError({'error':'name_required'})
    #     return data

class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = AuthorSerializer.Meta.fields+['image']
        read_only_fields = ['id']

class AuthorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','image']
        read_only_fields = ['id']
        extra_kwargs = {'image' : {'required': True}}

