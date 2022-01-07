import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from upload_csv.models import Bien


# Create your views here.
def stats(request):
    message = request.GET.get('message')
    data = pd.DataFrame(list(Bien.objects.all().values()))
    data = data[data.etage.notnull()]
    print(data.shape)
    result = pd.concat([data.groupby("ville")["prix_HT"].mean(), data.groupby("ville")["prix_HT"].std()], axis=1).round(2)
    result.insert(0, "ville", result.index)
    return render(request, "data_view/stats.html", {"columns": ['Ville', "Prix moyen", "Ecart type"], "data": result.values, "number": len(data), "std": data.prix_HT.std().round(2), "message": message})