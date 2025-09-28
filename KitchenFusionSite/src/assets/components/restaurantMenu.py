'''
Data structure of Menu of restaurant.
array of objects. each object has two or three keys: "category" and "items" and or "note". 
"items" is an array of tuple (3) ("item-name", price (sometimes object with variants price), "v/n", "description") 
v = veg, n = non-veg
"note" is a tuple of two coordinate: "note" text and price

'''
import json


MENU_BEVERAGES_SNACKS = [
    {
      "category": "aerated beverages", 
      "items": [
        ("tea", 20, "v", ""), 
        ("masala tea", 25, "v", ""), 
        ("coffee", 30, "v", ""), 
        ("water bottle", "on MRP", "v", ""),
        ("soft drinks", "on MRP", "v", "")
      ]
    },
    
    {
      "category": "mocktails", 
      "items": [
        ("virgin mojito", 59, "v", ""),
        ("blue lagoon", 59, "v", ""),
        ("kala khatta", 59, "v", ""),
        ("masala coke", 59, "v", ""),
        ("watermelon mojito", 59, "v", ""),
        ("kiwi mojito", 59, "v", ""),
        ("lemon ice tea", 59, "v", ""),
        ("peach ice tea", 59, "v", ""),
        ("fresh lime soda", 49, "v", ""),
        ("aam panna", 59, "v", ""),
        ("amrud panna", 59, "v", ""),
        ("banana shake", 59, "v", "")
      ]
    },
    
    {
      "category": "shakes",
      "items": [
        ("cold coffee", 59, "v", ""),
        ("chocolate shake", 69, "v", ""),
        ("vanilla shake", 69, "v", ""),
        ("strawberry shake", 69, "v", ""),
        ("oreo shake", 79, "v", ""),
        ("mango shake", 69, "v", ""),
        ("kit-kat shake", 79, "v", ""),
        ("dark chocolate shake", 79, "v", ""),
        ("banana shake", 49, "v", ""),
      ]
    },
    
    {
      "category": "soups",
      "items": [
        ("cream of tomato soup", 99, "v", ""),
        ("chicken soup", 99, "n", ""),
      ]
    },
    
    {
      "category": "salad",
      "items": [
        ("exotic vegetable salad", "99", "v", ""),
        ("egg salad", "99", "n", ""),
        ("egg & mayo salad", "99", "n", ""),
        ("chicken salad", "99", "n", ""),
      ]
    },
    
    {
      "category": "omelette", 
      "items": [
        ("indian spice omelette", 99, "n", ""),
        ("exotic vegetable omelette", 110, "n", ""),
        ("bread omelette", 120, "n", ""),
        ("chicken omelette", 130, "n", ""),
      ],
      "note": ("add on extra cheese & chicken", 30)
    },
    
    {
      "category": "sandwiches",
      "items": [
        ("classic veg grilled", 80, "v", "fusion with green vegetables"),
        ("bombay masala grilled", 80, "v", "fusion with aamchi masala"),
        ("classic cheese grilled", 90, "v", "fusion with cheese"),
        ("corn & cheese grilled", 90, "v", "fusion with corn & cheese"),
        ("paneer spicy grilled", 100, "v", "fusion with spicy cottage cheese"),
        ("classic chicken grilled", 109, "n", "chicken & vegetables"),
        ("egg & mayo grilled", 109, "n", "egg & mayonnaise"),
        ("chicken & mayo grilled", 109, "n", "chicken & mayonnaise"),
        ("chicken tikka grilled", 119, "n", "diced chicken with indian spices"),
      ],
      "note": ("add on extra cheese", 30)
    },
    
    {
      "category": "fries",
      "items": [
        ("french fries", 59, "v", ""),
        ("cheese & jalapenos fries", 59, "v", ""),
        ("peri peri french fries", 69, "v", ""),
        ("cheesy fries", 69, "v", ""),
      ]
    },
    
    {
      "category": "nuggets", 
      "items": [
        ("veg nuggets", 49, "v", ""),
        ("cheese balls nuggets", 59, "v", ""),
        ("potato nuggets", 59, "v", ""),
        ("onion rings", 69, "v", ""),
        ("chicken nuggets", 79, "n", ""),
        ("chicken fingers", 79, "n", ""),
        ("fish fingers", 79, "n", ""),
      ]
    },
    
    {
      "category": "maggi", 
      "items": [
        ("plain maggi", 49, "v", ""),
        ("masala maggi", 69, "v", ""),
        ("vegetable maggi", 79, "v", ""),
        ("masala cheese maggi", 89, "v", ""),
        ("chicken maggi", 89, "n", ""),
        ("cheese masala maggi", 109, "n", ""),
        ("chicken masala maggi", 119, "n", ""),
      ],
      "note": ("add on extra cheese", 30),
    },
    
    {
      "category": "pasta", 
      "items": [
        ("pasta in alfredo sause", 119, "v", ""),
        ("pasta in Arrabiata Sause", 119, "v", ""),
        ("pasta in mix sause", 129, "v", ""),
        ("mamma's secret pasta", 129, "v", ""),
        ("mac & cheese pasta", 139, "v", ""),
      ],
      "note": ("add on chicken", 49)
    },
    
    {
      "category": "burgers",
      "items": [
        ("aloo tikki burger", 49, "v", ""),
        ("veg tikki burger", 59, "v", ""),
        ("cheese ver burger", 69, "v", ""),
        ("crispy chicken burger", 109, "n", ""),
        ("grilled chicken burger", 109, "n", ""),
        ("tandoori chicken burger", 109, "n", ""),
        ("egg & mayo burger", 119, "n", ""),
      ]
    }, 
    
    {
      "category": "garlic bread",
      "items": [
        ("garlic bread", 59, "v", ""),
        ("cheese garlic bread", 69, "v", ""),
        ("cheese chilly garlic bread", 69, "v", ""),
        ("tandoori cheese garlic bread", 69, "v", ""),
      ],
      "note": ("add on extra cheese & chicken", 30)
    }, 
    
    {
      "category": "south indian cuisine",
      "items": [
        ("idli sambar (2 pcs)", 49, "v", ""),
        ("vada sambar (2 pcs)", 49, "v", ""),
        ("masala dosa", 69, "v", ""),
        ("plain dosa", 59, "v", ""),
        ("plain onion dosa", 59, "v", ""),
        ("plain butter dosa", 59, "v", ""),
        ("masala onion dosa", 69, "v", ""),
        ("butter masala dosa", 79, "v", ""),
        ("plain poddi dosa", 79, "v", ""),
        ("onion uttapam", 89, "v", ""),
        ("tomato uttapam", 89, "v", ""),
        ("onion tomato uttapam", 89, "v", ""),
        ("mix veg uttapam", 99, "v", ""),
        ("paneer masala dosa", 99, "v", ""),
        ("poddi masala dosa", 99, "v", ""),
        ("kitchen fusion special dosa", 99, "v", ""),
        ("mysore masala dosa", 109, "v", ""),
        ("cheese dosa", 109, "v", ""),
      ]
    },

    {
      "category": "combos",
      "items": [
        ("veg small pizza + garlic bread 3 pcs + 200ml Coke/Sprite", 199, "v", ""),
        ("non veg small pizza + garlic bread 3 pcs + 200ml Coke/Sprite", 249, "n", ""),
        ("veg burger + fries + 200ml Coke/Sprite", 149, "v", ""),
        ("chicken burger + fries + 200ml Coke/Sprite", 199, "n", ""),
        ("small dosa + idli + vada", 109, "v", ""),
        
      ]
    },
    
    {
      "category": "pizzas",
      "items": [
        ("corn & cheeze pizza", {"small": 99, "medium": 139, "large":199}, "v", "fusion with fresh corn"),
        ("onion & capsicum pizza", {"small": 99, "medium": 139, "large":199}, "v", "fusion with onion & capcicum"),
        ("classic margherita pizza", {"small": 99, "medium": 139, "large":199}, "v", "fusion with fresh cheese"),
        ("capsicum pizza", {"small": 99, "medium": 139, "large":199}, "v", "fusion with capsicum"),
        ("onion pizza", {"small": 99, "medium": 139, "large":199}, "v", "fusion with onion"),
        ("double cheese margherita pizza", {"small": 129, "medium": 239, "large":299}, "v", "fusion with cheese"),
        ("corn cheese & paneer pizza", {"small": 149, "medium": 190, "large":249}, "v", "fusion with corn & cottage cheese"),
        ("veg overload pizza", {"small": 159, "medium": 219, "large":299}, "v", "fusion with exotic vegetables"),
        ("farmhouse harvest pizza", {"small": 159, "medium": 219, "large":299}, "v", "fusion with onion, capsicum, corn, broccoli"),
        ("garden delight pizza", {"small": 159, "medium": 219, "large":299}, "v", "fusion with green vegetables"),
        ("paneer tikka pizza", {"small": 159, "medium": 219, "large":299}, "v", "fusion with cottage cheese & indian spices"),
        ("mushroom overload pizza", {"small": 179, "medium": 229, "large":319}, "v", "fusion with extra mushroom & cheese"),
        ("chicken tikka pizza", {"small": 159, "medium": 219, "large":299}, "n", "fusion with diced chicken & indian spices"),
        ("onion & chicken pizza", {"small": 159, "medium": 219, "large":299}, "n", "fusion with diced chicken & onion"),
        ("chicken delight pizza", {"small": 159, "medium": 219, "large":299}, "n", "fusion with diced chicken & exotic vegetables"),
        ("pepper & chicken pizza", {"small": 159, "medium": 219, "large":299}, "n", "fusion with diced chicken & bell pepper"),
        ("overloaded chicken pizza", {"small": 179, "medium": 229, "large":319}, "n", "fusion with extra extra chicken"),
        ("BBQ chicken pizza", {"small": 179, "medium": 229, "large":319}, "n", "fusion with diced chicken & indian spices "),
        ("chicken do pyaz pizza", {"small": 189, "medium": 219, "large":299}, "n", "fusion with diced chicken & indian spices"),
        ("chicken & mushroom pizza", {"small": 199, "medium": 239, "large":339}, "n", "fusion with chicken & mushroom"),
      ],
      "note": ("add on extra cheese", 30)
    },

  ]

# with open("RESTAURANT_MENU.json", "w") as f:
#   json.dump(MENU_BEVERAGES_SNACKS, f, indent=2)

