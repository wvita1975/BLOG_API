from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView): # este recurso permite ver la lista de elementos
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView): # este recurso permite ver, actualizar y eliminar un elemento
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    serializer_class = PostSerializer