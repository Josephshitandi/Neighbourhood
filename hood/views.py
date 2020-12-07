from django.shortcuts import render

# Create your views here.
def index(request):
    return render('index.html')

    
# class BusinessViewset(viewsets.ModelViewSet):
#     queryset = Business.objects.all()
#     serializer_class = BusinessSerializer
#     permission_classes = [IsAssigned, permissions.IsAdminUser]

    # def list(self, request, *args, **kwargs):
    #     self.get_queryset = Business.objects.filter(user=request.user)

    #     if request.user.is_superuser():
    #         self.get_queryset = Business.objects.all()

    #     super().list(*args, **kwargs)
