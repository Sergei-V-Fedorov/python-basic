import elementals

# базовые элементы
element_1 = elementals.Fire()
element_2 = elementals.Water()
element_3 = elementals.Terra()
element_4 = elementals.Air()
base_elements = [element_1, element_2, element_3, element_4]

for first_element in base_elements:
    for second_element in base_elements:
        result = first_element + second_element
        print(f"{first_element.name} + {second_element.name} = {result.name}")
