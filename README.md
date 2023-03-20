<h1>Tourbillon</h1>
<h2>Version: 0.1</h2>
<h2>(ScriptsRunner pour PinePhone)</h2>

<p>"Tourbillon est une application de gestion de scripts créée avec GTK3. Son interface conviviale et intuitive permet aux utilisateurs du PinePhone de gérer leurs scripts sans recourir à un terminal ou une application complexe. Conçue pour être simple et discrète, elle garantit l'efficacité de l'exécution de commandes simples ou multiples."</p>

<h2>Fonctionnalités</h2>

<ul>
  <li>L'application liste chaque script, depuis le dossier ~/Documents/Scripts.</li>
  <li>Sélectionner un ou plusieur scripts à exécuter.</li>
  <li>Cliquer sur le petit bouton en haut a droite pour exécuter les scripts selectionné.</li>
  <li><del>Ajouter, modifier et supprimer des scripts.</del></li>
  <li><del>Rechercher des scripts par nom ou par contenu.</del></li>
</ul>

<h2>Technologies utilisées</h2>

<ul>
  <li>GTK3</li>
  <li>Python</li>
</ul>

<h2>Test</h2>

<ul>
  <li>Matériel:     PinePhone</li>
  <li>Distribution: ArchlinuxARM <a href="https://github.com/dreemurrs-embedded/Pine64-Arch">dreemurrs-embedded/Pine64-Arch</a></li>
  <li>Environement: Phosh 0.25.2 (gnome-shell 43 pour mobile)</li>
  <li>Architecture: aarch64</li>
  <li>Status:       OK</li>
</ul>

<h2>Comment utiliser l'application</h2>

<ol>
  <li>Clonez le dépôt Tourbillon sur votre ordinateur. <p><code>git clone https://github.com/EliteScripts/Tourbillon.git</code></p></li>
  <li>Ouvrez un terminal et accédez au répertoire du projet. <p><code>cd Tourbillon</code></p></li>
  <li>Exécutez la commande suivante pour lancer l'application : <p><code>python scripts-runner.py</code></p></li>
  <li>Utilisez l'interface utilisateur pour exécuter vos scripts. <p><code>Enjoy</code></p></li>
</ol>

<h2>Contributions</h2>

<p>Les contributions sont les bienvenues ! Si vous souhaitez contribuer à Tourbillon, veuillez ouvrir une "pull request" avec vos modifications proposées.</p>

<p>N'oubliez pas de bien documenter votre code et de suivre les normes de codage PEP 8.</p>

<h2>Licence</h2>

<p>Tourbillon est distribué sous la licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.</p>
