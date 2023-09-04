from django.db import models

# Create your models here.
class Actor(models.Model):
    # 클래스 생성 시 자동으로 id라는 PrimaryKey가 생성
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    # movies =
    # movies라는 칼럼이 자동으로 등록
    # 자동으로 등록되는 이유? Movie클래스 내 actors 속성이
    # ManyToManyField로 관계설정(Actor, related_name='movies')이 되어있기 때문
    # Actor 클래스와 Movie 클래스의 actorts속성 간 M-N 관계설정이 되어 있음.
    
class Movie(models.Model):
    # 클래스 생성 시 자동으로 id라는 PrimaryKey가 생성
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    # categories = 
    # categories라는 칼럼이 자동으로 등록
    # 자동으로 등록되는 이유? Category클래스 내 movies 속성이
    # ManyToManyField로 관계설정(Movie, related_name='categories')이 되어있기 때문
    # Movie 클래스와 Category 클래스의 movies속성 간 M-N 관계설정이 되어 있음.
    
class Category(models.Model):
    # 클래스 생성 시 자동으로 id라는 PrimaryKey가 생성
    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie, related_name='categories')
    # Movie 클래스와 Category 클래스의 movies속성 간 M-N 관계설정이 되어 있음.

class User(models.Model):
    # 클래스 생성 시 자동으로 id라는 PrimaryKey가 생성
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

class Score(models.Model):
    # 클래스 생성 시 자동으로 id라는 PrimaryKey가 생성
    content = models.CharField(max_length=140)
    value = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # Movie 클래스와 Score 클래스의 movie속성 간 1-N 관계설정이 되어 있음.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # User 클래스와 Score 클래스의 user속성 간 1-N 관계설정이 되어 있음.