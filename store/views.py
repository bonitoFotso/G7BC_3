from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator 
from django.db.models import Q
from django.contrib import messages

def store():
    pass