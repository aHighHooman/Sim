
import Templates.MerchantTemplate as m
import Templates.itemTemplate as o


list = o.weaponList + o.ammoList

me = m.merchant(list)
me.greet()
me.askForNeeds()
need = int(input()) - 1
me.checkAvailability(need )
me.checkItemPrice(need )