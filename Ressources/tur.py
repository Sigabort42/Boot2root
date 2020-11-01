#!/usr/bin/env python

import turtle
import time

with open("./turtle", "r") as f:
    lines = f.readlines()
    instructions = [x.replace("Tourne", "").replace("degrees", "").replace("spaces", "").replace("de", "").strip() for x in lines]
    for line in instructions:
        if line == "Can you digest the message? :)":
            break
        nb = line.split(" ")
        del nb[0]
        if line != "":
            inst = "".join(nb)
            print("line", inst, line)
            inst = int(inst)
            if "Avance" in line:
                turtle.fd(inst)
            elif "Recule" in line:
                turtle.bk(inst)
            elif "gauche" in line:
                turtle.left(inst)
            elif "droit" in line:
                turtle.right(inst)
    time.sleep(10000)
