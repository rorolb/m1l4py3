from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.hp = randint(10, 100)
        self.power = randint(10, 100)

        Pokemon.pokemons[pokemon_trainer] = self



    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Картинка находится по пути: data['sprites']['front_default']
            return data['sprites']['other']['official-artwork']['front_default']
        else:
            # Возвращаем картинку Пикачу по умолчанию
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
            
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
                Здоровье: {self.hp}
                Сила: {self.power}"""

    def attack(self, enemy):
        if isinstance(враг, Волшебник): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            choise = randint(1,5)
            if choise == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

class Wizard(Pokemon):
    def attack(self, enemy):
        return super().attack(enemy)

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.сила -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "