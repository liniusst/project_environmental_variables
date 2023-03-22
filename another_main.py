from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {'DOMAIN': 'example.org', 'ADMIN_EMAIL': 'admin@example.org', 'ROOT_URL': 'example.org/app'}

# konfigas .env faile ir nurodom ko reikia atprintinti
print(config["ADMIN_EMAIL"])
print(config["USERNAME"])
print(config["PASSWORD"])

# jeigu panaudoti isvedime prideti $ zenkla pries variable