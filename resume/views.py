from ctypes import resize
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from resume import models,serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RelatedOrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from resume_collector007.users.models import User

class ResumeModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    serializer_class = serializers.ResumeSerializer
    filter_backends = [RelatedOrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    ordering_fields = '__all__'
    search_fields = [
        'information'

    ]
    filterset_fields = [
        'information'
    ]

    def get_clean_model_list(self,data,model):
        data = data.lower().title()
        data_list = []
        if ',' in data:
            data = data.split(',')
        else:
            data = [data]
        if data != '':
            print(data)
            for d in data:
                obj = model.objects.filter(name=d)
                if obj.exists():
                    obj = obj.first()
                    data_list.append(obj.id)
            return data_list
        return data_list

    def get_queryset(self):
        queryset = models.Resume.objects.all()
        skill_tags = self.request.query_params.get('skill_tags',None)
        general_tags = self.request.query_params.get('general_tags',None)
        if skill_tags:
            skill_tags = self.get_clean_model_list(skill_tags,models.SkillTag)
            queryset = queryset.filter(skill_tags__in=skill_tags).distinct()
        if general_tags:
            general_tags = self.get_clean_model_list(general_tags,models.GeneralTag)
            queryset = queryset.filter(general_tags__in=general_tags).distinct()
        return queryset

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

class GetUserChain(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def post(self,request):
        try:
            resume = models.Resume.objects.get(user__email=request.data['email'])
            data = {}
            while resume.reference:
                data[resume.user.email] = f'is refered by {resume.reference.email}'
                if resume.reference:
                    resume = models.Resume.objects.filter(user=resume.reference)
                    if resume.exists():
                        resume = resume.first()
                    else:
                        break

            return Response(data,status=status.HTTP_201_CREATED) 
        except Exception as e:
            print(e)
            return Response({'error':e},status=status.HTTP_400_BAD_REQUEST)