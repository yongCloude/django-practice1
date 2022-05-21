
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Book


class BookSeriralizer(serializers.Serializer) :
    bid = serializers.IntegerField(primary_key = True)
    title = serializers.ChaarField(max_length = 50)
    author = serializers.ChaarField(max_length = 50)
    category = serializers.ChaarField(max_length = 50)
    pages = serializers.IntegerField()
    price = serializers.IntegerField()
    published_date = serializers.DateField()
    description = serializers.TextField()

    
    def create(self, validated_data) :
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data) :
        instance.bid = validated_data.get('bid', instance.bid)
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.category = validated_data.get('category', instance.category)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.price = validated_data.get('price', instance.price)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.descripttion = validated_data.get('description', instance.description)
        instance.save()

        return instance