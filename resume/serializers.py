import imp
from rest_framework import serializers
from resume import models
from resume_collector007.users.models import User

class UserSeralizer(serializers.ModelSerializer):
        class Meta:
            model = models.User
            fields = ('email',)

class SkillTagSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.SkillTag
            fields = '__all__'

class GeneralTagSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.GeneralTag
            fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
        skill_tags = SkillTagSerializer(required=False,many=True,read_only=True)
        general_tags = GeneralTagSerializer(required=False,many=True,read_only=True)
        reference = UserSeralizer(required=False)
        reference_email = serializers.CharField(required=False)
        s_tags = serializers.CharField(required=False)
        g_tags = serializers.CharField(required=False)

        class Meta:
            model = models.Resume
            exclude = ('user',)

        def get_clean_model_list(self,data,model):
            data_list = []
            if ',' in data:
                data = data.split(',')
            else:
                data = [data]
            if data != '':
                for d in data:
                    skill,created = model.objects.get_or_create(name=d)
                    data_list.append(skill.id)
                return data_list
            return []

        def get_clean_reference(self,email):
            if email:
                user = User.objects.filter(email=email)
                if user.exists():
                    user = user.first()
                    return user
            return None
        
        def create(self, validated_data):
            s_tags = validated_data.pop('s_tags').lower().title()
            g_tags = validated_data.pop('g_tags').lower().title()
            skill_tags = self.get_clean_model_list(s_tags,models.SkillTag)
            general_tags = self.get_clean_model_list(g_tags,models.GeneralTag)
            validated_data['reference'] = self.get_clean_reference( validated_data.pop('reference_email'))
            validated_data['user'] = self.context['request'].user
            resume = models.Resume.objects.create(**validated_data)
            resume.skill_tags.add(*skill_tags)
            resume.general_tags.add(*general_tags)
            return resume