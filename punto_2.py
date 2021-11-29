from operator import itemgetter

ganaderia_caza_silvicultura = {'2002': 3265, '2003': 3532, '2004': 3389, 
                               '2005': 3530, '2006': 3226, '2007': 3143,
                               '2008': 3176, '2009': 3440, '2010': 3561,
                               '2011': 3634, '2012': 3622, '2013': 3549,
                               '2014': 3495, '2015': 3544, '2016': 3571,
                               }

comercio_hoteles_restaurantes = {'2002': 4042, '2003': 4205, '2004': 4220, 
                                 '2005': 4272, '2006': 4166, '2007': 4301,
                                 '2008': 4489, '2009': 4764, '2010': 5038,
                                 '2011': 5286, '2012': 5535, '2013': 5777,
                                 '2014': 5859, '2015': 6042, '2016': 6176,
                                 }
# for clave, valor in dnp.items():
    # print(f'{clave} --> {valor} ') 
mayor = (min(comercio_hoteles_restaurantes.items(), key = itemgetter(1))) 
menor = (max(ganaderia_caza_silvicultura.items(), key = itemgetter(1)))
