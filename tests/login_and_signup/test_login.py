import pytest
from config import Config
from src.pages.login_modal import LoginModal

@pytest.mark.login
class TestLogin:
    def test_successful_login(self, main_page):
        """
        Тест успешного входа в систему
        Шаги:
        1. Зайти на DEV_URL
        2. Дождаться загрузки страницы
        3. Обработать куки баннер
        4. Кликнуть на кнопку "Войти"
        5. Дождаться открытия модального окна
        6. Ввести email
        7. Ввести пароль
        8. Нажать кнопку "Войти"
        """
        # 1-3. Открытие страницы и обработка куки
        main_page.accept_cookies()
        
        # 4. Открытие модального окна входа
        main_page.open_login_modal()
        
        # Инициализация модального окна
        login_modal = LoginModal(main_page.driver)
        
        # 5. Проверка видимости модального окна
        assert login_modal.is_modal_visible(), "Модальное окно входа не отображается"
        
        # 6-8. Ввод учетных данных и отправка формы
        login_modal.login(Config.DEV_USER, Config.DEV_PASSWORD)

        
        
        # Здесь можно добавить проверки успешного входа
        # Например, проверить появление элемента, который виден только после входа