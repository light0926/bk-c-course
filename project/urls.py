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

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from project import views

router = DefaultRouter()
router.register(r"project", views.ProjectViewSet)

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"project-user/", views.UserProjectContactViewSet.as_view({"post": "create"})),
    path(
        r"project-user/<int:project_id>/",
        views.UserProjectContactViewSet.as_view(
            {"post": "bulk_import", "get": "get_all_user_info", "delete": "destroy"}
        ),
    ),
    path(
        r"project-user/<int:project_id>/student/",
        views.UserProjectContactViewSet.as_view({"get": "get_all_stu_info"}),
    ),
    path(
        r"project-user/<int:project_id>/teacher/",
        views.UserProjectContactViewSet.as_view({"get": "get_all_tea_info"}),
    ),
    path(
        r"project-user/<int:project_id>/export-info/",
        views.UserProjectContactViewSet.as_view({"get": "export_info"}),
    ),
]
