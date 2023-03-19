<h1>Tourbillon (ScriptsRunner pour PinePhone)</h1>

<p>Tourbillon est une application de gestion de scripts créée avec GTK3. Cette application est principalement destinée aux utilisateurs du PinePhone (téléphone Linux) pour leur permettre de gérer facilement des scripts en leur offrant une interface utilisateur simple et conviviale.</p>

<h2>Fonctionnalités</h2>

<ul>
  <li>Exécuter des scripts à partir de l'application sur votre PinePhone.</li>
  <li>Permet de sélectionner un script ou plusieur en même temps, à exécuter en un clic.</li>
  <li>Modification de chaque script, depuis le dossier ~/Documents/Scripts.</li>
  <li><del>Ajouter, modifier et supprimer des scripts.</del></li>
  <li><del>Rechercher des scripts par nom ou par contenu.</del></li>
</ul>

<h2>Technologies utilisées</h2>

<ul>
  <li>GTK3</li>
  <li>Python</li>
</ul>

<h2>Comment utiliser l'application</h2>

<ol>
  <li>Installez les dépendances nécessaires pour l'exécution de l'application.</li>
  <li>Clonez le dépôt Tourbillon sur votre ordinateur.</li>
  <li>Ouvrez un terminal et accédez au répertoire du projet.</li>
  <li>Exécutez la commande suivante pour lancer l'application : python scripts-runner.py</li>
  <li>Utilisez l'interface utilisateur pour gérer vos scripts.</li>
</ol>


<h2>Dépendances nécessaires</h2>
<p>Debian/Ubuntu</p>
<code>sudo apt-get install python3-gi python3-gi-cairo gir1.2-gtk-3.0</code>
<p>ArchLinux/Manjaro</p>
<code>sudo pacman -S python-gobject gtk3</code>
<p>Fedora</p>
<code>sudo dnf install python3-gobject gtk3</code>
<p>Mageia</p>
<code>sudo urpmi python3-gobject gtk3</code>

<h2>Contributions</h2>

<p>Les contributions sont les bienvenues ! Si vous souhaitez contribuer à Tourbillon, veuillez ouvrir une "pull request" avec vos modifications proposées.</p>

<p>N'oubliez pas de bien documenter votre code et de suivre les normes de codage PEP 8.</p>

<h2>Licence</h2>

<p>Tourbillon est distribué sous la licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.</p>
