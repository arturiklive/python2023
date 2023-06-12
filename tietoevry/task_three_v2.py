a = {
    "book": "142645",
    "identifier": [
        {"type": "ABC", "value": "3806768526"},
        {"type": "DEF", "value": "97789689"},
    ],
}


def check_type_exists(check):
    search_value = check
    item_key = None
    if "identifier" in a:
        for item in a["identifier"]:
            if "type" in item and item["type"] == search_value:
                item_key = item["value"]
                break
    if item_key is not None:
        print(f"Item with value '{search_value}' exists. Key: {item_key}")
    else:
        print(f"No item with value '{search_value}' found.")


check_type_exists("ABC")