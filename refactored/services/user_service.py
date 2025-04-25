class UserService:
    @staticmethod
    def find_user_by_name(users, name):
        for user in users:
            if user.name == name:
                return user
        return None
