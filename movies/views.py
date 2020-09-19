<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm
from .models import Movie
# Create your views here.


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    #template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"


class AddReviews(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent', None))
            form.save()
        return redirect(movie.get_abs_url())
>>>>>>> Stashed changes
