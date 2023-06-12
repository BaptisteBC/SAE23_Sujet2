from django.shortcuts import render
from django.http import FileResponse
from fpdf import FPDF
from . import models, views

def film_pdf(request, id):
    film = models.Film.objects.get(pk=id)

    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    note = views.note_moy(id)

    # Add the film poster (affiche)
    if film.affiche:
        poster_path = film.affiche.path  # Retrieve the file path of the affiche image
        pdf.image(poster_path,x=(pdf.w - 67.5) / 2, h=100, w=67.5)

    # Add the film details
    pdf.set_font("Arial", '', 15)
    pdf.cell(200, 10, txt=f"Titre du film: {film.titre}", ln=1, align='C')
    pdf.cell(200, 10, txt=f"Année de sortie: {film.annee_sortie}", ln=2, align='C')
    pdf.cell(200, 10, txt=f"Réalisateur: {film.realisateur}", ln=3, align='C')
    pdf.cell(200, 10, txt=f"Categorie: {film.categorie}", ln=4, align='C')
    pdf.cell(200, 10, txt=f"note moyenne: {note}/5", ln=5, align='C')
    pdf.cell(200, 10, txt="", ln=1, align='C')


    # Add the actors who played in the film
    acteurs = models.Film_Acteur.objects.filter(film=film)
    if len(acteurs) == 0:
        pdf.set_font("Arial", '', 10)
        pdf.cell(200, 10, txt="Aucun acteur n'a joué dans ce film.", ln=7, align='C')
    else:
        pdf.set_font("Arial", '', 15)
        pdf.cell(200, 10, txt="Acteurs ayant joué dans ce film:", ln=7, align='C')
        for actor in acteurs:
            pdf.set_font("Arial", '', 10)
            pdf.cell(200, 10, txt=f"{actor.acteur.nom} {actor.acteur.prenom}", ln=8, align='C')

    coms = models.Commentaire.objects.filter(film=film)
    pdf.set_font("Arial", '', 15)
    pdf.cell(200, 10, txt="", ln=1, align='C')
    pdf.cell(200, 10, txt="Commentaire:", ln=1, align='C')
    if len(coms) == 0:
        pdf.cell(200, 10, txt="Aucun commentaires ont été posté pour ce film", ln=9, align='C')
    else:
       
        for com in coms:
            pdf.set_font("Arial", '', 10)
            pdf.cell(200, 10, txt="", ln=1, align='C')
            pdf.cell(200, 10, txt=f"{com.personne}", ln=1, align='C')
            pdf.cell(200, 10, txt=f"note: {com.note}/5", ln=1, align='C')
            pdf.cell(200, 10, txt=f"{com.commentaire}", ln=1, align='C')
            pdf.cell(200, 10, txt=f"{com.date}", ln=1, align='C')

    pdf.output(f"media/filmographie/pdf/{film.titre}.pdf")  # Set the PDF filename with the film's title
    response = FileResponse(open(f"media/filmographie/pdf/{film.titre}.pdf", 'rb'))
    return response
