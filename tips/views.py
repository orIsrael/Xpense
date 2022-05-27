from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tip
from .forms import TipForm
<<<<<<< HEAD
=======

>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)
from .constants import (
    TIPS_PAGE_ROUTE,
    ADD_TIP_PAGE_ROUTE,
    EDIT_TIP_PAGE_ROUTE,
    READ_MORE_PAGE_ROUTE,
    CATEGORIES_PAGE_ROUTE,
    DATE_PAGE_ROUTE,
<<<<<<< HEAD
=======
    # SHOW_PROFILE_ROOT,
>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)
)


def index(request):
    tips = Tip.objects.order_by('-date')
    return render(request, TIPS_PAGE_ROUTE, {'tips': tips})


@login_required
def add_tip(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tips')
    else:
        form = TipForm()
    return render(request, ADD_TIP_PAGE_ROUTE, {'form': form})


def filter_tip_by_category(request, category):
    category_filtered_tips = Tip.objects.filter(category=category)
    return render(
        request, CATEGORIES_PAGE_ROUTE, {'category': category, 'category_filtered_tips': category_filtered_tips}
    )


def filter_tip_by_date(request, date):
    datetime_object = datetime.strptime(date, "%Y-%m-%d")
    filtered_tips_by_date = Tip.objects.all().filter(
        date__year=datetime_object.year, date__month=datetime_object.month, date__day=datetime_object.day
    )
    return render(request, DATE_PAGE_ROUTE, {'date': date, 'filtered_tips_by_date': filtered_tips_by_date})


def read_more_view(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    return render(request, READ_MORE_PAGE_ROUTE, {'tip': tip})


<<<<<<< HEAD
=======
# def show_profile_view(request, user_id):
#     return redirect(SHOW_PROFILE_ROOT)


>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)
@login_required
def edit_tip(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    form = TipForm(request.POST or None, instance=tip)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            tip = form.save(commit=False)
            tip.save()
            context = {'form': form}
            return redirect('/tips')
    else:
        form = TipForm()
    return render(request, EDIT_TIP_PAGE_ROUTE, context)


@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    if tip.user_token == User.get_session_auth_hash:
        tip.delete()
        return redirect('/tips')
    else:
        raise PermissionDenied()
