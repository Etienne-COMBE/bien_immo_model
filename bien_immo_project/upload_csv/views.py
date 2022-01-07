from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
import pandas as pd
from .models import Bien
import json

# Create your views here.
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)
    if (user is not None) and user.has_perm('upload'):
        return render(request, "upload_csv/index.html")
    elif user is not None:
        message = "Wrong permissions"
        return redirect(f"stats/?message={message}")
    return redirect("/")

def data_prep(df):
    df.nb_piece.astype(int)
    mois_dict = {"janvier": "Jan",
             "fevrier": "Feb",
             "mars": "Mar",
             "avril": "Apr",
             "mai": "May",
             "juin": "Jun",
             "juillet": "Jul",
             "aout": "Aug",
             "septembre": "Sep",
             "octobre" : "Oct",
             "novembre": "Nov",
             "decembre": "Dec"}
    for key in mois_dict:
        df.date_fin_programme = df.date_fin_programme.str.replace(key, mois_dict[key])
    df.parking = df.parking.astype(bool)
    return df.copy()

def save_data(request):
    if request.method == 'POST':
        file = request.FILES["csv_file"]
        df_og = pd.read_csv(file, sep = ",", parse_dates=["date_extraction"]).iloc[:, 1:]
        df = data_prep(df_og)
        df = df[~df.balcony]
        data = json.loads(df.to_json(orient="records"))
        Bien.objects.all().delete()
        for record in data:
            bien = Bien.objects.create(
                            id_lot = record["id_lot"],
                            nb_piece = record["nb_piece"],
                            typologie = record["typologie"],
                            prix_tva_reduite = record["prix_tva_reduite"],
                            prix_tva_normale = record["prix_tva_normale"],
                            prix_HT = record["prix_HT"],
                            prix_m2_HT = record["prix_m2_HT"],
                            prix_m2_TTC = record["prix_m2_TTC"],
                            surface = record["surface"],
                            etage = record["etage"],
                            orientation = record["orientation"],
                            exterieur = record["exterieur"],
                            balcony = record["balcony"],
                            garden = record["garden"],
                            parking = record["parking"],
                            nom_programme = record["nom_programme"],
                            ville = record["ville"],
                            departement = record["departement"],
                            date_fin_programme = record["date_fin_programme"],
                            adresse_entiere = record["adresse_entiere"],
                            promoteur = record["promoteur"],
                            date_extraction = record["date_extraction"])
            bien.save()
    return redirect("stats")