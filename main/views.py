from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406355640',
        'name': 'Roberto Eugenio Sugiarto',
        'class': 'PBP E',
    }

    return render(request, "main.html", context)
