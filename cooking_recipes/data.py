import json

def process_json(fpath):
    with open(fpath, 'r') as f:
        data = json.load(f)

    for d in data:
        with open(f"text_data/{d['name']}.txt", 'w') as f:
            f.write("Recipe name: " + d['name'] + '\n\n')
            f.write("Number of servings: " + str(d['num_served']) + '\n\n')
            ingrediants = ["  " + str(ii['amount']) + ' ' + ii['units'] + ' ' + ii['description']
                           for ii in d['ingredients']]
            f.write("Ingredients:\n" + "\n".join(ingrediants) + '\n\n')
            f.write("Directions: " + ' '.join(d['directions']) + '\n')

if __name__ == "__main__":
    process_json('data/vegetarian.json')
    process_json('data/desert.json')
    process_json('data/fish.json')
    process_json('data/meat.json')
    process_json('data/misc.json')
