from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=200)

# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Superhero(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    superpower = models.CharField(max_length=100)
    is_good = models.BooleanField()
    is_male = models.BooleanField()
    rating = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name
        
        

class Animal(models.Model):
    name = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=200)
    is_male = models.BooleanField()
    
    def __str__(self):
        return self.name 
        

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)
    
class Stock(models.Model):
    company = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    market_cap = models.FloatField()
    
    def __str__(self):
        return self.company
        

class Artist(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
        
    
class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class Country(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField()
    
    def __str__(self):
        return self.name
        
    
class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class NBATeam(models.Model):
    name = models.CharField(max_length=255)
    worth = models.IntegerField()
    
    def __str__(self):
        return self.name
        
    
class NBAAthlete(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(NBATeam, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
