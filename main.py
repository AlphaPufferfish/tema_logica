import sys
from treelib import Node, Tree
tree = Tree()
smn = ['∧', '∨', '⇒', '⇔']
prop = input()
prop = list(prop)
prop2 = prop.copy()
poz = [0] * len(prop)
semne = 0
pd = 0
pi = 0
imax = 0
lp = []

# verificarea corectitudinii in conformitate cu definitia

for i in range(len(prop)):
    if prop[i] == '(':
        pd += 1
        lp.append(i)
    if prop[i] == ')':
        pi += 1
    if prop[i] == '¬' or prop[i] in smn:
        semne += 1
        poz[i] = pd-pi
        if pd - pi > imax:
            imax = pd - pi
        if prop[i] == '¬':
            if ord('A') <= ord(prop[i+1]) <= ord('Z'):
                poz[i+1] = pd-pi
                poz[i+2] = pd-pi
                poz[i-1] = pd-pi
        if prop[i] in smn:
            if ord('A') <= ord(prop[i - 1]) <= ord('Z'):
                poz[i-1] = pd-pi
                poz[i-2] = pd-pi
            if ord('A') <= ord(prop[i + 1]) <= ord('Z'):
                poz[i+1] = pd-pi
                poz[i+2] = pd-pi

if len(prop) == 1 and ord('A') <= ord(prop[0]) <= ord('Z'):
    print('Sirul este formula propozitionala')
    sys.exit()
if semne != pd or semne != pi or semne == 0:
    print('Sirul nu este formula propozitionala')
    if semne < pd or semne < pi:
        print('Apar paranteze in plus')
    else:
        print('Lipsesc paranteze')
    sys.exit()
else:
    for i in reversed(lp):
        if prop[i+1] == '¬':
            if ord('A') <= ord(prop[i + 2]) <= ord('Z') and prop[i + 3] == ')':
                prop[i] = 'A'
                for j in range(3, 0, -1):
                    prop.pop(i+j)
            elif prop[i+2] == '(':
                pass
            else:
                print('Sirul nu este formula propozitionala, sintaxa este gresita')
                sys.exit()
        else:
            if ord('A') <= ord(prop[i + 1]) <= ord('Z') and ord('A') <= ord(prop[i + 3]) <= ord('Z') and prop[i+2] in smn:
                prop[i] = 'A'
                for j in range(4, 0, -1):
                    prop.pop(i+j)
if len(prop) == 1:
    print('Sirul este formula propozitionala')
else:
    print('Sirul nu este formula propozitionala, sintaxa este gresita')
    sys.exit()

# reprezentarea grafica a arborelui
for rang in range(1, imax + 1):
    for pozitie in range(len(poz)):
        if poz[pozitie] == rang:
            if rang == 1:
                if prop2[pozitie] in smn:
                    tree.create_node(prop2[pozitie], pozitie)
                    pozprec = pozitie
                    poz[pozitie] = 0
                    if ord('A') <= ord(prop2[pozitie + 1]) <= ord('Z'):
                        tree.create_node(prop2[pozitie + 1], pozitie + 1, parent=pozitie)
                        poz[pozitie+1] = 0
                        poz[pozitie+2] = 0
                    if ord('A') <= ord(prop2[pozitie - 1]) <= ord('Z'):
                        tree.create_node(prop2[pozitie - 1], pozitie - 1, parent=pozitie)
                        poz[pozitie-1] = 0
                        poz[pozitie-2] = 0
                if prop2[pozitie] == '¬':
                    tree.create_node(prop2[pozitie], pozitie)
                    pozprec = pozitie
                    poz[pozitie] = 0
                    poz[pozitie-1] = 0
                    if ord('A') <= ord(prop2[pozitie + 1]) <= ord('Z'):
                        tree.create_node(prop2[pozitie + 1], pozitie + 1, parent=pozitie)
                        poz[pozitie+1] = 0
                        poz[pozitie+2] = 0
            else:
                if prop2[pozitie] in smn:
                    tree.create_node(prop2[pozitie], pozitie, parent=pozprec)
                    poz[pozitie] = 0
                    if ord('A') <= ord(prop2[pozitie + 1]) <= ord('Z'):
                        tree.create_node(prop2[pozitie + 1], pozitie + 1, parent=pozitie)
                        poz[pozitie + 1] = 0
                        poz[pozitie+2] = 0
                    if ord('A') <= ord(prop2[pozitie - 1]) <= ord('Z'):
                        tree.create_node(prop2[pozitie - 1], pozitie - 1, parent=pozitie)
                        poz[pozitie - 1] = 0
                        poz[pozitie - 2] = 0
                if prop2[pozitie] == '¬':
                    tree.create_node(prop2[pozitie], pozitie, parent=pozprec)
                    poz[pozitie] = 0
                    poz[pozitie-1] = 0
                    if ord('A') <= ord(prop2[pozitie + 1]) <= ord('Z'):
                        tree.create_node(prop2[pozitie + 1], pozitie + 1, parent=pozitie)
                        poz[pozitie + 1] = 0
                        poz[pozitie + 2] = 0
            if rang not in poz:
                pozprec = pozitie

tree.show()
