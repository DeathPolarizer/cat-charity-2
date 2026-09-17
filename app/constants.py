# DB
NAME_LENGTH_DB = 100

# User creation
TOKEN_LIFETIME = 3600
PASSWORD_MIN_LENGTH = 3
PASSWORD_WITHOUT_EMAIL = "Пароль не может содержать ваш email"
USER_CREATED = "Пользователь {email} зарегистрирован."

# Validators errors
PROJECT_EXISTS = "Проект с таким именем:{} уже существует!"
PROJECT_NOT_FOUND = "Проекта с id:{} не найден"
FULL_AMOUNT_TOO_LOW = (
    "Нельзя установить значение full_amount меньше уже вложенной суммы."
)
PROJECT_CLOSED = "Закрытый проект нельзя редактировать!"
PROJECT_HAS_INVESTMENTS = (
    "Запрещено удаление проектов, в которые уже внесены средства!"
)
