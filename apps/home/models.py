# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.

# class Employee(models.Model):
#     EmpId = models.CharField(max_length=3)
#     EmpName = models.CharField(max_length=200)
#     EmpGender = models.CharField(max_length=10)
#     EmpEmail = models.EmailField()
#     EmpDesignation = models.CharField(max_length=150)
#     class Meta:
#         db_table="Employee"

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id = models.IntegerField()
    response = models.CharField(max_length=255)
    score = models.DecimalField(max_digits=15, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    assessment_id = models.IntegerField()
    recommendations = models.TextField(max_length=255)
    weight = models.DecimalField(max_digits=15, decimal_places=6)
    section_id = models.IntegerField()
    class Meta:
        db_table="answer"

class Assessments(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.CharField(max_length=255)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    customer_first_name = models.CharField(max_length=255)
    customer_last_name = models.CharField(max_length=255)
    personal_id = models.CharField(max_length=255)
    customer_age = models.IntegerField()
    sex = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=15, decimal_places=6)
    lon = models.DecimalField(max_digits=15, decimal_places=6)
    loan_purpose = models.IntegerField()
    loan_section = models.IntegerField()
    status = models.IntegerField()
    total_score = models.DecimalField(max_digits=15, decimal_places=6)
    region_name = models.CharField(max_length=255)
    score_ratio = models.DecimalField(max_digits=15, decimal_places=6)
    class Meta:
        db_table="assessments"

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    first_names = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="users"

class Questions(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    placeholder = models.CharField(max_length=512)
    questions = models.CharField(max_length=1028)
    scores = models.CharField(max_length=255)
    type = models.IntegerField()
    section = models.IntegerField()
    active = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    has_recommendations  = models.IntegerField()
    group = models.IntegerField()
    category = models.IntegerField()
    order = models.IntegerField()
    recommendation_by_score = models.CharField(max_length=1028)
    recommendation_score = models.DecimalField(max_digits=15, decimal_places=6)
    related = models.IntegerField()
    trigger_related_val = models.CharField(max_length=255)

    class Meta:
        db_table="questions"

class Question_category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    class Meta:
        db_table="question_category"

class Question_groups(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    class Meta:
        db_table="question_groups"

class Question_types(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    active = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="question_types"

class Results(models.Model):
    id = models.IntegerField(primary_key=True)
    assessment_id = models.IntegerField()
    answers = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="results"

class Scenario(models.Model):
    scenario_id = models.IntegerField(primary_key=True)
    scenario_name = models.CharField(max_length=255)
    scenario_description = models.TextField()
    risk_exposure_value = models.DecimalField(max_digits=15, decimal_places=6)
    class Meta:
        db_table="scenario"

class Sections(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(max_digits=15, decimal_places=6)
    class Meta:
        db_table="sections"
class Loan_purposes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="loan_purposes"

class Loan_section(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    importance_value = models.DecimalField(max_digits=15, decimal_places=6)
    class Meta:
        db_table="loan_section"