class PasswordManagerError(Exception):
    pass

class EntryNotFoundError(PasswordManagerError):
    pass

class EntryAlreadyExistsError(PasswordManagerError):
    pass
