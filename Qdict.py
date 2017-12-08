#-*- coding: utf-8 -*-

def get_qdict():
    d = {
    'price':[
    ['Quel est votre budget ?','int'],
    ['Quel budget souhaitez vous investir ?',['50~100','100~200','200~300','300~500','500~700','700~1000','1000-2000'],'interval',[[50-100],[100-200],[200-300],[300-500],
	[500-700],[700-1000],[1000-2000]]]
    ],
    'OS':[
    ['Quel système d\'exploitation souhaiteriez vous ?','union'],
    ['Quel système d\'exploitation souhaiteriez vous ?',['Android','iOS','aucune importance'],'union',['Android','ios']]
    ],
    'weight':[
    ['Un téléphone lourd vous dérange t-il ?','fbool'],
    ['Souhaiteriez vous un téléphone ?',['lourd','normal','léger','pas d\'importance'],'fbool',['1','0,5','0','0,5']]
    ],
    'photo':[
    ['La photographie est-elle importante pour vous','fbool'],
    ['Pour l\'apareil photo :',['Je suis fan de snapchat','Je prend les photos aux repas de famille','Je n\'utilise pas l\'appareil photo'],'fbool',['1','0,5','0']]
    ],
    'memory':[
    ['De quelles capacités de stockage avez vous besoin ?','int'],
    ['Remplissez vous votre téléphone de photo/jeux video ?',['Oui','Non','Moyennement'],'interval',['1','0','0,5']]
    ],
    'sim':[
    ['Quel type de carte sim souhaitez vous/avez vous ?','text'],
    ['Quel type de carte sim souhaitez vous ?',['Nano SD','micro SD'],'fbool',['1','0']]
    ],
    'battery_amp':[
    ['Etes vous toujours près d\'une prise avec votre chargeur ?','fbool'],
    ['A quel point utilisez vous votre téléphone durant la journée ?',['Tout le temps','De temps en temps','jamais'],'fbool',['1','0,5','0']]
    ],
    'size':[
    ['utilisez vous votre téléphone pour regarder Youtube ou la télévision ?','fbool'],
    ['Avez vous besion d\'un grand écran ?',['Oui','Non','pas vraiment'],'fbool',['1','0','0,5']]
    ],
    'moveable_battery':[
    ['Aurez vous besoin de retirer la batterie ?','fbool'],
    ['Shouaitez vous une baterie amovible ?',['Oui','Non','Peu importe'],'fbool',['1','0','0,5']]
    ],
    'memory_upgrade':[
    ['Shouaitez vous pouvoir augmenter la mémoire de votre téléphone quand vous le souhaitez ?','fbool'],
    ['Aurez vous besoin d\'utilisez une carte mémoire suplémentaire ?',['Oui','Non','Sans importance'],'fbool',['1','0','0,5']]
    ]
    }
    return d
