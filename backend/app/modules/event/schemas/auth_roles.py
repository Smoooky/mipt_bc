import enum

class AuthRoles(str, enum.Enum):
    MEMBER = 'member'
    ORGANIZER = 'organizer'
    MANAGER = 'manager'
    ADMIN = 'admin'