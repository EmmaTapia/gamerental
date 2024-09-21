from django.shortcuts import render, get_object_or_404, redirect
from .models import VideoGame, Platform, Genre, Rental, Platform, Customer
from .forms import  PlatformForm

def index(request):
    return render(request, 'base.html')


def add_platform(request):
    if request.method == 'POST':
        form = PlatformForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_platforms') 
    else:
        form = PlatformForm()
    return render(request, 'add_platform.html', {'form': form})

def list_platforms(request):
    platforms = Platform.objects.all()
    return render(request, 'list_platforms.html', {'platforms': platforms})



def list_video_games(request):
    video_games = VideoGame.objects.all()
    genres = Genre.objects.all()
    platforms = Platform.objects.all()
    return render(request, 'list_video_games.html', {
        'video_games': video_games,
        'genres': genres,
        'platforms': platforms,
    })


def register_video_game(request):
    platforms = Platform.objects.all()
    genres = Genre.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        platform_id = request.POST.get('platform')
        genre_id = request.POST.get('genre')
        stock = request.POST.get('stock')

        platform = Platform.objects.get(id=platform_id)
        genre = Genre.objects.get(id=genre_id)

        video_game = VideoGame(
            title=title,
            platform=platform,
            genre=genre,
            stock=stock
        )
        video_game.save()
        return redirect('list_video_games') 

    return render(request, 'register_video_game.html', {
        'platforms': platforms,
        'genres': genres
    })

def register_rental(request):
    video_games = VideoGame.objects.all()

    if request.method == 'POST':
        video_game_id = request.POST.get('video_game')
        renter_name = request.POST.get('renter_name')
        rental_date = request.POST.get('rental_date')
        return_date = request.POST.get('return_date')

        rental = Rental(
            video_game_id=video_game_id,
            renter_name=renter_name,
            rental_date=rental_date,
            return_date=return_date
        )
        rental.save()
        return redirect('list_rentals')

    return render(request, 'register_rental.html', {
        'video_games': video_games
    })

def list_rentals(request):
    rentals = Rental.objects.all()
    return render(request, 'list_rentals.html', {'rentals': rentals})


def video_games_by_platform(request, platform_id):
    platform = Platform.objects.get(id=platform_id)
    video_games = VideoGame.objects.filter(platform=platform)
    genres = Genre.objects.all()
    platforms = Platform.objects.all()
    return render(request, 'video_games_by_platform.html', {
        'video_games': video_games,
        'genres': genres,
        'platforms': platforms,
        'selected_platform': platform,
    })


def video_games_by_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    video_games = VideoGame.objects.filter(genre=genre)
    genres = Genre.objects.all()
    platforms = Platform.objects.all()
    return render(request, 'video_games_by_genre.html', {
        'video_games': video_games,
        'genres': genres,
        'platforms': platforms,
        'selected_genre': genre,
    })