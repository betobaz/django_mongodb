from django.db import models

"""
Our yummy stuff
"""
class Product( models.Model ):
	name = models.CharField( max_length=200 )
	vintage = models.CharField( max_length=200 )
	production = models.IntegerField( 'Amount produce in volum' )
	bottles = models.IntegerField( 'Number of bottles produced' )

"""
Real cool dude(ttes)
"""
class Customer( models.Model ):
	first_name = models.CharField( max_length=200 )
	last_name = models.CharField( max_length=200 )

"""
How our inventors afford nice cars...
"""
class Purchase( models.Model ):
	date_ordered = models.DateTimeField( 'Date purchase' )
	date_processed = models.DateTimeField( 'Date processed' )
	date_delivered = models.DateTimeField( 'Date delivered' )
	product = models.ForeignKey( Product )
	customer = models.ForeignKey( Customer )
