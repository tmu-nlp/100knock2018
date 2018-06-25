from django.shortcuts import render
import requests
from .function import search_aliases_name, search_area, search_artist, search_tag


def search_artists(request):
    search = request.GET.get('search')
    limit = request.GET.get('limit')
    mode = request.GET.get('mode')
    if search:
        limit = int(limit)
        if mode == 'artist_name':
            context = {
                'result': search_artist(search, limit),
            }
        elif mode == 'area':
            context = {'result': search_area(search, limit)}
        elif mode == 'aliases_name':
            context = {'result': search_aliases_name(search, limit)}
        elif mode == 'tag':
            context = {'result': search_tag(search, limit)}
    else:
        context = {}

    return render(request, 'search_artists/search.html', context)
