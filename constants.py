class Urls:
    BASE = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    DELETE_COURIER = '/api/v1/courier/'
    CREATE_ORDER = '/api/v1/orders'
    PARAMS_FOR_GET_ORDER = '?limit=5&page=0&nearestStation=["110"]'


class Messages:
    SUCCESS_CREATE = '{"ok":true}'
    DUPLICATE_COURIER = 'Этот логин уже используется. Попробуйте другой.'
    WITHOUT_REQUIRED_FIELD = 'Недостаточно данных для создания учетной записи'
    LOGIN_WITHOUT_REQUIRED_FIELD = 'Недостаточно данных для входа'
    LOGIN_WITH_INCORRECT_DATA = 'Учетная запись не найдена'
