from Templates.MerchantTemplate import merchant

import Templates.ObjectTemplate as o
from Templates.HumanTemplate import human

list = o.weaponList + o.ammoList

Merchant = merchant(list)
