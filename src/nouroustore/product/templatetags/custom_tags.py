from django import template

register = template.Library()

def calcul_remise(price,remise):
    'Calcul price - remise '
    #product.price - (product.price* (product.remise/100) ) 
    return price-(price*(remise/100))

register.filter('calcul_remise', calcul_remise)