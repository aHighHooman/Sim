
import Templates.MerchantTemplate as m
import Templates.ObjectTemplate as o


list = o.weaponList + o.ammoList

me = m.merchant(list)
me.askForNeeds()