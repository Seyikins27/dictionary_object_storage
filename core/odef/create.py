class Create:
    username=""
    password=""
    conf_file="../../bin/config/global.pkl"
    message=""

    def __init__(self, username, password, confirm_password):
        if not password==confirm_password:
            self.message="Passwords do not match"
        return self.message

    def start(self):
        return

    def conf_file_exists(self):
        return

    def user_exists(self):
        return