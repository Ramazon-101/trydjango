from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Recipe, RecipeIngredient
from .forms import RecipesForm, RecipeIngredientForm
from django.forms import modelform_factory


def recipe_list_view(request):
    recipes = Recipe.objects.all()

    context = {
        'objects_list': recipes
    }

    return render(request, 'recipes/list.html', context)


def recipe_detail_view(request, slug=None):
    obj = None
    if slug is not None:
        obj = Recipe.objects.get(slug=slug)

    context = {
        'object': obj
    }

    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_create_view(request):
    form = RecipesForm(request.POST or None)
    form2 = RecipeIngredientForm(request.POST or None)
    if form.is_valid() and form2.is_valid():
        obj = form.save(commit=False)
        obj.user_id = request.user.id
        obj.save()
        form.save_m2m()

        obj2 = form2.save(commit=False)
        obj2.recipe_id = obj.id
        obj2.save()
        return redirect('recipes:detail', obj.slug)

    context = {
        'form': form,
        'form2': form2,

    }

    return render(request, 'recipes/create.html', context)


def recipe_edit_view(request, pk=None):
    obj = None
    context = {

    }

    if pk is not None:
        obj = Recipe.objects.get(id=pk)
        obj2 = RecipeIngredient.objects.get(recipe_id=obj.id)
        form = RecipesForm(request.POST or None, instance=obj)
        form2 = RecipeIngredientForm(request.POST or None, instance=obj2)
        context['form'] = form
        context['form2'] = form2
        if form.is_valid() and form2.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            obj.save()
            form.save_m2m()

            obj2 = form2.save(commit=False)
            obj2.recipe_id = obj.id
            obj2.save()
            return redirect('recipes:detail', obj.slug)

    return render(request, 'recipes/edit.html', context)


def recipe_delete_view(request, pk=None):
    context = {

    }

    return render(request, 'recipes/delete.html', context)
