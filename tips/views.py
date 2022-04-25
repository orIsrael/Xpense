from django.shortcuts import render, redirect, get_object_or_404
from .models import Tip
from .forms import TipForm
from .constants import TIPS_PAGE_ROUTE, ADD_TIP_PAGE_ROUTE, EDIT_TIP_PAGE_ROUTE, READ_MORE_PAGE_ROUTE,\
    CATEGORIES_PAGE_ROUT


def board(request):
    tips = Tip.objects.order_by('-date')
    return render(request, TIPS_PAGE_ROUTE, {'tips': tips})


def add_tip(request):
    if request.method == "POST":
        form = TipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tips')
    else:
        form = TipForm()
    return render(request, ADD_TIP_PAGE_ROUTE, {'form': form})


def categories_filter(request, cats):
    category_filtered_tips = Tip.objects.filter(category=cats)
    return render(request, CATEGORIES_PAGE_ROUT, {'cats': cats, 'category_filtered_tips': category_filtered_tips})


def read_more_view(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    return render(request, READ_MORE_PAGE_ROUTE, {'tip': tip})


def edit_tip(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    form = TipForm(request.POST or None, instance=tip)
    context = {'form': form}
    if request.method == "POST":
        if form.is_valid():
            tip = form.save(commit=False)
            tip.save()
            context = {'form': form}
            return redirect('/tips')
    else:
        form = TipForm()
    return render(request, EDIT_TIP_PAGE_ROUTE, context)


def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    tip.delete()
    return redirect('/tips')
