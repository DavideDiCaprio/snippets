"""
abstract base classes (ABC)

 ABCs provide a way to define abstract interfaces that derived classes must implement
 you cannot instantiate an abstract class directly
 child classes must implement all abstract methods defined in the parent ABC
 ensure consistency across related classes
"""

from abc import ABC, abstractmethod

class GameCharacter(ABC):
    """
    Abstract base class representing a video game character.
    
    This class serves as a blueprint/interface that all character classes must implement.
    It cannot be instantiated directly.
    """
    
    def __init__(self, name, level=1):
        """
        Initialize with attributes that all game characters will have
        """
        self.name = name
        self.level = level
        self.health = 100
        self.is_alive = True
    
    @abstractmethod
    def attack(self, target):
        """
        Abstract method that defines how this character attacks targets.
        
        Every child class MUST implement this method.
        """
        pass

    @abstractmethod
    def special_ability(self):
        """
        Abstract method that defines this character's unique special ability.
        
        Every child class MUST implement this method.
        """
        pass
    
    # Concrete methods that all characters will inherit
    def take_damage(self, amount):
        """
        Concrete method that all child classes inherit without needing to override.
        """
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            return f"{self.name} has been defeated!"
        return f"{self.name} took {amount} damage! Health: {self.health}"
    
    def heal(self, amount):
        """Another concrete method available to all child classes"""
        if not self.is_alive:
            return f"{self.name} is defeated and cannot be healed!"
        
        self.health += amount
        if self.health > 100:
            self.health = 100
        return f"{self.name} healed for {amount} points! Health: {self.health}"
    
    def level_up(self):
        """Increase character level"""
        self.level += 1
        return f"{self.name} leveled up to level {self.level}!"


# Concrete implementations of the GameCharacter ABC

class Warrior(GameCharacter):
    """Warrior implementation of the GameCharacter ABC"""
    
    def __init__(self, name, weapon, level=1):
        super().__init__(name, level)  # Call parent constructor
        self.weapon = weapon
        self.strength = 10 + self.level * 2
        self.health = 120  # Warriors have more health
    
    def attack(self, target):
        """Implementation of the required abstract method"""
        damage = self.strength + (self.level * 3)
        target.take_damage(damage)
        return f"{self.name} attacked {target.name} with their {self.weapon} for {damage} damage!"
    
    def special_ability(self):
        """Implementation of the required abstract method"""
        self.health += 20
        return f"{self.name} used Battle Cry and gained 20 health! Current health: {self.health}"


class Mage(GameCharacter):
    """Mage implementation of the GameCharacter ABC"""
    
    def __init__(self, name, spell_book, level=1):
        super().__init__(name, level)
        self.spell_book = spell_book
        self.mana = 100
        self.intelligence = 12 + self.level * 3
    
    def attack(self, target):
        damage = self.intelligence + (self.level * 2)
        target.take_damage(damage)
        return f"{self.name} cast a spell on {target.name} for {damage} damage!"
    
    def special_ability(self):
        if self.mana >= 30:
            self.mana -= 30
            return f"{self.name} cast Arcane Explosion! All enemies take 50 damage. Mana remaining: {self.mana}"
        return f"{self.name} doesn't have enough mana to cast Arcane Explosion!"
    
    # Adding a class-specific method
    def regenerate_mana(self, amount):
        self.mana += amount
        if self.mana > 100:
            self.mana = 100
        return f"{self.name} regenerated {amount} mana. Current mana: {self.mana}"


# Demonstration of ABC usage

# This would raise TypeError: Can't instantiate abstract class GameCharacter with abstract methods attack, special_ability
# generic_character = GameCharacter("Player", 5)

# Create concrete game character instances
aragorn = Warrior("Aragorn", "Andúril", 5)
gandalf = Mage("Gandalf", "Book of Spells", 7)

# Basic interactions
print(aragorn.attack(gandalf))
print(gandalf.take_damage(15))  # Using inherited method
print(gandalf.special_ability())

# Level up example
print(aragorn.level_up())

#  polymorphism - treating different types through their common ABC interface
characters = [aragorn, gandalf]
enemy = Warrior("Orc Leader", "Battle Axe", 3)

print("\nAll characters use their special abilities:")
for character in characters:
    print(character.special_ability())

print("\nAll characters attack the enemy:")
for character in characters:
    print(character.attack(enemy))

print(f"\nEnemy status: Health={enemy.health}, Is alive={enemy.is_alive}")