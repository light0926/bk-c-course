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

from django.urls import path

from project_task import views

from .perform_task_views import PerformAndJudgeViewSet

urlpatterns = [
    path(
        r"project-task/",
        views.ProjectTaskList.as_view(
            {"post": "create_task", "delete": "bulk_delete_task"}
        ),
    ),
    path(
        r"project-task/<int:project_task_id>/",
        views.ProjectTaskList.as_view(
            {"patch": "update_task", "delete": "delete_task"}
        ),
    ),
    path(
        r"project-task/<int:project_id>/student/all/",
        PerformAndJudgeViewSet.as_view({"get": "get_all_stu_task"}),
    ),
    path(
        r"project-task/<int:project_id>/teacher/all/",
        PerformAndJudgeViewSet.as_view({"get": "get_all_task"}),
    ),
    path(
        r"project-task/<int:project_task_id>/teacher/",
        PerformAndJudgeViewSet.as_view({"get": "get_single_task_detail_tea"}),
    ),
    path(
        r"project-task/<int:project_task_id>/student/",
        PerformAndJudgeViewSet.as_view({"get": "get_single_task_detail_stu"}),
    ),
    path(
        r"project-task-info/<int:project_task_id>/stu-info/<int:student_id>/",
        PerformAndJudgeViewSet.as_view({"get": "get_stu_info"}),
    ),
    path(
        r"project-task-info/<int:project_task_id>/",
        PerformAndJudgeViewSet.as_view(
            {"patch": "perform_task", "get": "get_individual_info"}
        ),
    ),
    path(
        r"project-task-info/<int:project_task_id>/judge/<int:student_id>/",
        PerformAndJudgeViewSet.as_view(
            {
                "patch": "judge_task",
            }
        ),
    ),
]
