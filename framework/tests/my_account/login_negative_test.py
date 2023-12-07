import pytest
from framework.src.pages.MyAccontSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)


        my_account.go_to_my_account()
        my_account.input_login_username('hello')
        my_account.input_login_password('A2@sdasdasdas')
        my_account.click_login_button()

        # verify error message
        expected_error = 'Error: The username hello is not registered on this site.'
        my_account.wait_until_error_is_displayed(expected_error)
