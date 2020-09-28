#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了兼容python2.7（django企业开发实战指出）
from __future__ import unicode_literals

from django.db import models

from apps.qa_platform.enumeration import (
    REQUEST_METHOD, EVENT_API_STUTAS, CHECK_METHOD, HTTP_CONTENT_TYPE
)

# 自定义序列化类
from apps.common.serializers import query_set_list_serializers

class ApiCaseDataNode(models.Model):
    # 用例id
    id = models.AutoField(primary_key=True)
    # 关联用例表
    data_id = models.IntegerField(verbose_name='所属数据id', default=1)
    # 用例模型id
    model_id = models.IntegerField(verbose_name='所属用例模型id')
    # 请求头
    headers = models.TextField(verbose_name="请求头", default="{}")
    # url后的请求参数
    params = models.TextField(verbose_name="请求行入参", default="{}")
    # 入参
    body = models.TextField(verbose_name="请求体入参", default="{}")
    # mock状态（0 不启用mock，1启用mock）
    is_mock = models.BooleanField(verbose_name="mock状态（0 不启用mock，1启用mock）", default=False)
    # mock返回
    mock_response = models.TextField(verbose_name="mock的返回值", default="{}")
    # 表达式状态
    is_expression = models.BooleanField(verbose_name="表达式状态：0 不启用jsonpath捕捉参数化\n 1 启用jsonpath捕捉参数化", default=False)
    # 用例描述
    text = models.CharField(verbose_name="用例描述", max_length=64, blank=True, null=True)
    # 状态（启用/不启用）
    is_status = models.BooleanField(verbose_name="启用状态：0未启用 1启用", default=True)
    # 逻辑删除
    is_delete = models.BooleanField(verbose_name="逻辑删除：1删除 0未删除", default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_case_data_node"
        # django的admin界面的后台展示的数据
        verbose_name = "用例参数"
        verbose_name_plural = verbose_name

    @classmethod
    def query_case_api_data_node_list_by_data_id(cls,data_id: int):
        return query_set_list_serializers(
            cls.objects.filter(
                data_id=data_id,
                is_status=1,
                is_delete=0
            )
        )