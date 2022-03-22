from django import template

register = template.Library()

def calcul_remise(price,remise):
    'Calcul price - remise '
    return '{0:.2f}'.format(price-(price*(remise/100)))

register.filter('calcul_remise', calcul_remise)