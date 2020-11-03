La faille de kernel connu dirtyCow permet a un attaquant qui opere sur la machine cible de passer root en exploitant le sous systeme kernel COW (Copy & Write).

Plusieurs façon d'exploiter cette faille sont disponibles dans le lien github en dessous
https://github.com/dirtycow/dirtycow.github.io/wiki/PoCs

Plus de Détails:

Une condition de concurrence a été trouvée dans la façon dont le sous-système de mémoire du kernel Linux a géré la rupture de copie sur écriture (COW) des mappages de mémoire privée en lecture seule. Un utilisateur local non privilégié pourrait utiliser cette faille pour obtenir un accès en écriture à des mappages de mémoire autrement en lecture seule et ainsi augmenter ses privilèges sur le système. C'était l'une des vulnérabilités d'escalade de privilèges les plus sérieuses jamais découvertes et elle affectait presque toutes les principales distributions Linux jusqu'a Linux Kernel < 3.19.0-73.8


