import icecream

icecream.make_icecream('chocolate', 'sprinkles', 'nuts', 'whipped cream')

#importing icecream module , we got all the functions defined in icecream.py

# You can also import specific functions from the module
from icecream import make_icecream
# Now you can use the make_icecream function directly
make_icecream('vanilla', 'chocolate chips', 'caramel drizzle')


# We can also import the entire module and use it with a prefix
import icecream as ic
ic.make_icecream('strawberry', 'fresh fruit', 'chocolate syrup')

# We can also import specific functions from the module with an alias
from icecream import make_icecream as mc
# Now you can use the make_icecream function with the alias
mc('mint', 'oreo crumbs', 'chocolate flakes')

# You can also import all functions from the module
from icecream import *
# Now you can use all functions defined in the icecream module without a prefix
make_icecream('cookie dough', 'caramel bits', 'marshmallows')
