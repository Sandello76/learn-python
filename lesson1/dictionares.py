example ={"city": "Москва", "temperature": "20"} 
print(example["city"])
example["temperature"] = str(int(example["temperature"]) - 5)
print(example)
print(example.get("country", "Россия"))
example["date"] = "27.05.2019"
print(len(example))