titulo = input("Ingrese el titulo para su pagina web: ")
slug = titulo.lower().replace(' ', '-').replace('?', '').replace('!', '').replace('.', '').replace(',', '').replace(':', '').replace(';', '').strip('-')
print(f"Slug: {slug}")
print(f"URL: https://misitio.com/blog/{slug}")