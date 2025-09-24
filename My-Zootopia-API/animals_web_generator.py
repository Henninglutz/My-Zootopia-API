import json
import data_fetcher


#load from the file (same project) and return json
def load_data(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


#check all values and getting them in variables
def serialize_animal(animal: dict) -> str:
    characteristics = animal.get("characteristics") or {}            #dict available?
    name = animal.get("name") or "(?)"
    diet = characteristics.get("diet") or "(n/a)"
    animal_type = characteristics.get("type") or "(n/a)"
    locations = animal.get("locations") or []
#just the first location, changed after review
    first_location = locations[0] if isinstance(locations, list) and locations else "(n/a)"

    return (
        '<li class="cards__item">'                                   #preparing li
        f"<strong>Name:</strong> {name}<br/>\n"
        f"<strong>Diet:</strong> {diet}<br/>\n"
        f"<strong>Location:</strong> {first_location}<br/>\n"
        f"<strong>Type:</strong> {animal_type}<br/>\n"
        "</li>"
    )

#loop for all and returning the html content
def generate_html(animals: list[dict]) -> str:
    if not animals:
        return '<li class="cards__item"><em>No animals found.</em></li>'
    return "\n".join(serialize_animal(a) for a in animals)


def user_info_animal():
    name = str(input("Enter a animal name to add all informations to the databank - by magic **#*+#* :")).strip()
    if not name:
        raise ValueError("No animal, sorry!")
    return name


#gets data from nfetcher (milestone3) and build html
def main():

    data_path = "animals_data.json"
    template_path = "animals_template.html"
    output_path = "animals.html"

    name = user_info_animal()
    animals = data_fetcher.fetch_data(name)
    print(type(animals), len(animals))
    items_html = generate_html(animals)

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", items_html)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        print(f"Done, wrote {output_path}")

if __name__ == "__main__":
    main()