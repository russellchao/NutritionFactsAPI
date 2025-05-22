import requests
from private import appID, apiKey # hidden from public


def get_total_nutrition():
    pass



def get_nutrition_facts(item):

    # Testing with apple
    url = f"https://api.edamam.com/api/nutrition-data?app_id={appID}&app_key={apiKey}&ingr={item}"
    response = requests.get(url)

    nutrition_data = response.json()

    # DEBUG
    print(nutrition_data)


    quantity = nutrition_data['ingredients'][0]['parsed'][0]['quantity']
    food = nutrition_data['ingredients'][0]['parsed'][0]['food']
    calories = nutrition_data['ingredients'][0]['parsed'][0]['nutrients']['ENERC_KCAL']['quantity']
    weight = nutrition_data['ingredients'][0]['parsed'][0]['weight']
    


    print(f"Quantity: {quantity}")
    print(f"Food: {food}")
    print(f"Calories (in kcal): {calories}")
    print(f"Weight (in g): {weight}")

    
    

  





if __name__ == "__main__":


    get_nutrition_facts("1 apple")


    # while True:
    #     pass
