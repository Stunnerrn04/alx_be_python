# Prompt the user to input the current weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Provide clothing recommendations based on the input
if weather == "sunny":
    recommendation = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    recommendation = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."
else:
    recommendation = "Sorry, I don't have recommendations for this weather."

# Output the recommendation
print(recommendation)
