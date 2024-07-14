import streamlit as st
import webbrowser
import streamlit.components.v1 as com


# Exemple de contenu supplémentaire -----------------------
com.html(""" <html>
  <head>
<style>
.animated_rainbow_2 {
    font-size = 42px;
    font-family: cursive;
    text-align :left;
    padding:1px;
    height: 100px;
    -webkit-animation: animatedBackground_b 3s linear infinite alternate;
}

@keyframes animatedBackground_b{
    0% {color: #ff8b00;}
    10% {color: #e8ff00}
    20% {color: #5dff00}
    30% {color: #00ff2e}
    40% {color: #00ffb9}
    50% {color: #00b9ff}
    60% {color: #002eff}
    70% {color: #5d00ff}
    80% {color: #e800ff}
    90% {color: #ff008b}
    100% {color: #ff0000}
}
</style>
  </head>
   
   <p class="animated_rainbow_2"> <font size =9>  👩‍⚕️👨‍⚕️ Bienvenue sur notre tableau de bord interactif pour surveiller la santé régionale 🩺 🩺  </font></p>
   <title> this is a title </title>
</body> 
</html>
""")












# Afficher le titre animé

# Afficher l'animation Lottie

# Fonction pour ouvrir le lien dans une nouvelle fenêtre de navigateur
def open_link(url):
    webbrowser.open_new_tab(url)

# Titre de l'application
st.subheader("Redirection vers d'autres sites Web")

# Bouton 1
if st.button("Aller vers Shiny site 2    (travail personnel) "):
    open_link("https://razantejjar.shinyapps.io/Shiny-generation/")

# Bouton 2 (exemple de site web fictif)
if st.button("Aller vers Shiny site 1   (projet académique) "):
    open_link("https://razantejjar.shinyapps.io/Analyses-Covide/")
