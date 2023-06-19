from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Bookmark
from datetime import datetime
# Create your views here.

def bookmark_list(request, un):
    count = 0
    link_list = Bookmark.objects.filter(candidatemail=un).values()
    for coun in link_list:
        count = count + 1

    now = datetime.now() # current date and time
    today_dt = now.strftime("%A, %B %d, %Y %I:%M:%S %p")
    hour = now.strftime("%H")
    hour_int = int(hour)
    if hour_int < 12:
        greeting = "Good morning"
    elif hour_int < 16:
        greeting = "Good afternoon"
    elif hour_int <= 23:
        greeting = "Good evening"

    context = {"link": link_list, "count": count, "today_datetime": today_dt, "greeting": greeting}
    return render(request, "bookmarkdatabase/home.html", context)

def add(request):
    links_list = Bookmark.objects.all().values()
    context = {"links": links_list}
    return render(request, "bookmarkdatabase/add.html", context)

def addlink(request, un):
    x = request.POST["link"]
    y = request.POST["linkname"]
    z = request.POST["mail"]
    link = Bookmark(link=x, linkname=y, candidatemail=z)
    link.save()
    return redirect("/home/" + un)

def deleteLink(request, un):
    count = 0
    link_list = Bookmark.objects.filter(candidatemail=un).values()
    for coun in link_list:
        count = count + 1

    context = {"link": link_list, "count": count}
    return render(request, "bookmarkdatabase/deleteLink.html", context)

def delete_view(request, id, un):
    link = Bookmark.objects.get(id=id)
    link.delete()
    return redirect("/home/" + un)

def update_page(request, un):
    count = 0
    link_list = Bookmark.objects.filter(candidatemail=un).values()
    for coun in link_list:
        count = count + 1

    context = {"link": link_list, "count": count}
    return render(request, "bookmarkdatabase/updateLink.html", context)

def update(request, id):
    link = Bookmark.objects.get(id=id)
    context = {"updateItem": link}
    return render(request, "bookmarkdatabase/update.html", context)

def updaterecord(request, id, un):
    URL = request.POST["link"]
    displayname = request.POST["linkname"]
    update_link = Bookmark.objects.get(id=id)
    update_link.link = URL
    update_link.linkname = displayname
    update_link.save()
    return redirect("/home/" + un)



