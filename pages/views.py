from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import About
from .forms import AboutForm

def about_view(request):
    about = About.objects.first()
    return render(request, "pages/about.html", {"about": about})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_about(request):
    about, created = About.objects.get_or_create(id=1)
    if request.method == "POST":
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect("about_page") 
    else:
        form = AboutForm(instance=about)
    return render(request, "pages/page_form.html", {"form": form})






