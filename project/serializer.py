# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from rest_framework import serializers

from project.models import Project, UserProjectContact


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        extra_kwargs = {
            "introduction": {"required": False},
            "creator": {"required": False},
            "updater": {"required": False},
        }


class PartialProjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=90, required=False)
    introduction = serializers.CharField(required=False)
    property = serializers.CharField(max_length=90, required=False)
    category = serializers.CharField(max_length=90, required=False)
    organization = serializers.CharField(max_length=90, required=False)
    creator = serializers.CharField(max_length=90, required=False)
    updater = serializers.CharField(max_length=90, required=False)
    create_time = serializers.DateTimeField(required=False)
    update_time = serializers.DateTimeField(required=False)


class UserProjectContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProjectContact
        exclude = ["id"]
        extra_kwargs = {"project_id": {"write_only": True}}
