import math
sales_results = {
    "Johnver": {
        "revenue": {
            "tea": 190,
            "coffe": 325,
            "water": 682,
            "milk": 829
        },
        "expenses": {
            "tea": 120,
            "coffe": 300,
            "water": 50,
            "milk": 67
        },
     },
    "Vanston": {
        "revenue": {
            "tea": 140,
            "coffe": 19,
            "water": 14,
            "milk": 140
        },
        "expenses": {
            "tea": 65,
            "coffe": 10,
            "water": 299,
            "milk": 254
        }
    },
    "Danbree": {
        "revenue": {
            "tea": 1926,
            "coffe": 293,
            "water": 852,
            "milk": 609
        },
        "expenses": {
            "tea": 890,
            "coffe": 23,
            "water": 1290,
            "milk": 89
        }
    },
    "Vansey": {
        "revenue": {
            "tea": 14,
            "coffe": 1491,
            "water": 56,
            "milk": 120
        },
        "expenses": {
            "tea": 54,
            "coffe": 802,
            "water": 12,
            "milk": 129
        }
    },
    "Mundyke": {
        "revenue": {
            "tea": 143,
            "coffe": 162,
            "water": 659,
            "milk": 87
        },
        "expenses": {
            "tea": 430,
            "coffe": 235,
            "water": 145,
            "milk": 76
        }
    }
}

for name, sales in sales_results.items():
    commission = 0 
    for drink_name, drink_sales in sales["revenue"].items():
        profit = drink_sales - sales["expenses"][drink_name]
        if profit > 0:
           commission += profit * 0.062
           floor_val = math.floor(commission)
    print(name, ":", floor_val)
    
     
       
            
