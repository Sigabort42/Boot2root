
Les ROP est un technique d'exploitation qui consiste a selectionner des bout de code "gadget" qui seront executer un a un. Cela permet dans certain cas de bypass certaine migitation comme la GNU_STACK non executable ou l'ASLR.
Pour pouvoir faire un execve il faut trouver quelque primitive comme ecrire dans eax, ebx, ...
Certain gadget se trouve dans la libc et d'autre dans dans le linker dynamic ld.so
Après la selection des gadget il faut faire attention au null byte car c'est la function strcpy qui est utilisé.
