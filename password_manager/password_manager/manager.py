from .exceptions import EntryNotFoundError, EntryAlreadyExistsError

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_entry(self, name, password):
        if name in self.passwords:
            raise EntryAlreadyExistsError(f"Entry '{name}' already exists.")
        self.passwords[name] = password

    def remove_entry(self, name):
        if name not in self.passwords:
            raise EntryNotFoundError(f"Entry '{name}' not found.")
        del self.passwords[name]

    def get_password(self, name):
        if name not in self.passwords:
            raise EntryNotFoundError(f"Entry '{name}' not found.")
        return self.passwords[name]
