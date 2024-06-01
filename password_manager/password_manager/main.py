import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .manager import PasswordManager
from .exceptions import EntryNotFoundError, EntryAlreadyExistsError

class PasswordManagerApp(toga.App):

    def startup(self):
        self.manager = PasswordManager()

        # Основное окно
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Поле ввода имени
        self.name_input = toga.TextInput(placeholder='Entry Name', style=Pack(flex=1))
        main_box.add(self.name_input)

        # Поле ввода пароля
        self.password_input = toga.TextInput(placeholder='Password', style=Pack(flex=1))
        main_box.add(self.password_input)

        # Кнопки
        button_box = toga.Box(style=Pack(direction=ROW, padding=5))
        add_button = toga.Button('Add', on_press=self.add_entry, style=Pack(flex=1))
        get_button = toga.Button('Get', on_press=self.get_password, style=Pack(flex=1))
        remove_button = toga.Button('Remove', on_press=self.remove_entry, style=Pack(flex=1))
        button_box.add(add_button)
        button_box.add(get_button)
        button_box.add(remove_button)
        main_box.add(button_box)

        # Поле для вывода сообщений
        self.message_label = toga.Label('Message:', style=Pack(padding_top=10))
        main_box.add(self.message_label)

        # Установить содержимое окна
        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()

    def add_entry(self, widget):
        name = self.name_input.value
        password = self.password_input.value
        try:
            self.manager.add_entry(name, password)
            self.message_label.text = f"Entry '{name}' added successfully."
        except EntryAlreadyExistsError as e:
            self.message_label.text = str(e)

    def get_password(self, widget):
        name = self.name_input.value
        try:
            password = self.manager.get_password(name)
            self.message_label.text = f"Password for '{name}': {password}"
        except EntryNotFoundError as e:
            self.message_label.text = str(e)

    def remove_entry(self, widget):
        name = self.name_input.value
        try:
            self.manager.remove_entry(name)
            self.message_label.text = f"Entry '{name}' removed successfully."
        except EntryNotFoundError as e:
            self.message_label.text = str(e)

def main():
    return PasswordManagerApp('Password Manager', 'org.example.passwordmanager')

if __name__ == '__main__':
    main().main_loop()
