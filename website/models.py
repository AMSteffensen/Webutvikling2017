# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




## LOGIN
## A database model for the UserCridentials table
class UserCredential(models.Model):
    # user_id - Is automatically added by django
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    verified = models.BooleanField()


## USERS
## A database model for the Contractor(Talenter) table
class Contractor(models.Model):
    #contractor_id - Is automatically added by Django
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)
    ## TODO - Interests(tag)
    """
    This can be easily implemented with a quick and dirty solution.
    Store each interest in a single string separated by a prefix.
    When displaying the tags, simply split the string by the prefix.
    Remove a tag? Search for the substring and remove it.
    Add a tag? Append it to the end.
    Sorting the tags is an easy way to display the tags nicely.
    """
    ## TODO - Competence Categories
    """
    This can probably be executed the same way as the interest tags.
    """


## A database model for the Principal(Oppdragsgiver) table
class Principal(models.Model):
    # principal_id - Is automatically added by Django
    company = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)
    ## Address information
    county = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    street = models.CharField(max_length=255)
    ## TODO - Interests(tag)
    """
    This can be easily implemented with a quick and dirty solution.
    Store each interest in a single string separated by a prefix.
    When displaying the tags, simply split the string by the prefix.
    Remove a tag? Search for the substring and remove it.
    Add a tag? Append it to the end.
    Sorting the tags is an easy way to display the tags nicely.
    """
    ## TODO - Competence Categories
    """
    This can probably be executed the same way as the interest tags.
    """
	
	
## JOBS
## A database model for the Jobs(Posted by Principals) table
class Job(models.Model):
    # job_id - Is automatically added by Django
    jobName = models.CharField(max_length=250)
    jobDescription = models.TextField(max_length=10000)
    ## TODO - Requirements(tag)
    """
    This can be easily implemented with a quick and dirty solution.
    Store each interest in a single string separated by a prefix.
    When displaying the tags, simply split the string by the prefix.
    Remove a tag? Search for the substring and remove it.
    Add a tag? Append it to the end.
    Sorting the tags is an easy way to display the tags nicely.
    """
    ## TODO - JobDeadline
    """
    This can be stored in a variety of ways.
    As a timestamp for a future time.
    As a date.
    As plain text.
    """
    jobAuthor = models.ForeignKey(Principal)
    jobTaken = models.BooleanField()