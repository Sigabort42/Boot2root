Le buffer Overflow est le fait d'exploiter une faille venant du developpement d'un programme.

Un espace memoire de 64 octets (par exemple) est alloué par le programme.

En écrivant plus de 64 octets dans le buffer, on peux prendre le controle de l'execution du programme et ainsi ouvrir un shell (par exemple) par le biais d'un shellcode ou en exploitant la libc. C'est ce que nous allons faire ici

En faisant pointé EIP sur l'addresse de la fonction system de la libc cette derniere sera executé.

Encore faut t'il lui envoyé les parametres qu'il faut, dans notre cas "/bin/sh"

L'exploit se compose ainsi

[140 * 'B'][address de system][OSEF][address de "/bin/sh"]

La stack se compose ainsi

eip actuelle				-> address de system
eip à la sortie de la fonction system	-> OSEF
argument de system    	       		-> address de "/bin/sh"