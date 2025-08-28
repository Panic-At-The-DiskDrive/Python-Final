from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import ModelForm

from .models import Game, Developer, Platform


def model_field_names(model):

    names = []
    for f in model._meta.get_fields():
  
        if getattr(f, 'auto_created', False):
            continue

        if getattr(f, 'many_to_many', False):
            continue

        if getattr(f, 'one_to_many', False) and getattr(f, 'auto_created', False):
            continue

        name = getattr(f, 'name', None)
        if not name:
            continue
        names.append(name)

    exclude = {'id', 'pk', 'created_at', 'updated_at'}
    return [n for n in names if n not in exclude]


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = model_field_names(Game)


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = model_field_names(Developer)


class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = model_field_names(Platform)


def home(request):

    latest = Game.objects.all().order_by('-pk')[:6]
    return render(request, 'games/home.html', {'latest_games': latest})


def list_games(request):

    q = request.GET.get('q', '').strip()
    if q:
        games = Game.objects.filter(title__icontains=q)
    else:
        games = Game.objects.all()
    return render(request, 'games/list_games.html', {
        'games': games,
        'query': q,
    })


def game_detail(request, pk):

    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})


@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES or None)
        if form.is_valid():
            game = form.save()
            messages.success(request, 'Juego creado correctamente.')
            return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm()
    return render(request, 'games/add_game.html', {'form': form})


@login_required
def add_developer(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Desarrollador creado correctamente.')
            return redirect('add_game')
    else:
        form = DeveloperForm()
    return render(request, 'games/add_developer.html', {'form': form})


@login_required
def add_platform(request):
    if request.method == 'POST':
        form = PlatformForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Plataforma creada correctamente.')
            return redirect('add_game')
    else:
        form = PlatformForm()
    return render(request, 'games/add_platform.html', {'form': form})

@login_required
def edit_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES or None, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, 'Juego actualizado correctamente.')
            return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm(instance=game)
    return render(request, 'games/edit_game.html', {'form': form})

@login_required
def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.delete()
        messages.success(request, 'Juego eliminado correctamente.')
        return redirect('list_games')
    return render(request, 'games/confirm_delete.html', {'game': game})
