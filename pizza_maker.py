#Created by: Michael Taylor
#Created on: October 14, 2017
#Created for ICS3U
#This program calculates the cost of a pizza

import ui

HST = .13
size_price = 10.00
toppings_price = 0

#called when any button is pressed, action is dependant on sender
def touch_up_inside(sender):
	global size_price
	if sender.name == 'large_button':
		size_price = 6.50
	if sender.name == 'extra_large_button':
		size_price = 10
	calculate_total_cost()
	
def calculate_cost_of_toppings(sender):
	global toppings_price
	toppings_price = 1 + int((view['toppings_slider'].value * 4.4)-1)*0.75
	view['number_of_toppings_label'].text = str(int((view['toppings_slider'].value) * 4.4))
	if int((view['toppings_slider'].value)*4.4) == 0:
		toppings_price = 0
	calculate_total_cost()
	
def calculate_total_cost():
	globals()
	view['subtotal_label'].text = 'Subtotal: ' + '${:,.2f}'.format(size_price + toppings_price)
	view['hst_label'].text = 'HST: ' + '${:,.2f}'.format((size_price + toppings_price)*HST)
	view['total_label'].text = 'Total: ' + '${:,.2f}'.format((size_price + toppings_price)*(1+HST))

view = ui.load_view()
view.present('sheet')
