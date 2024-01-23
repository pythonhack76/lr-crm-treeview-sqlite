from faker import Faker

fake = Faker()

# Numero di dati fittizi da generare
num_data_to_generate = 100  # Modifica questo valore a tuo piacimento

# Lista per memorizzare i dati fittizi generati
data_list = []

for _ in range(num_data_to_generate):
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_id = fake.random_int(min=1000, max=9999)
    fake_address = fake.street_address()
    fake_city = fake.city()
    fake_state = fake.state()
    fake_zipcode = fake.zipcode()

    data = [fake_first_name, fake_last_name, fake_id, fake_address, fake_city, fake_state, fake_zipcode]
    data_list.append(data)

# Stampare la lista di dati fittizi generati con virgola dopo la parentesi quadra chiusa
for idx, data in enumerate(data_list, start=1):
    print(f"{data},")
