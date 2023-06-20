from user import User
from post import Post

user_one = User("ziad@zz.com", "ziad", "pwd1", "DevOps Engineer")
user_one.get_user_info()

user_two = User("mohamed@mm.com", "Mohamed", "pwd2", "Developer")
user_two.get_user_info()

new_post = Post("on a secret mission today", user_two.name)
new_post.get_post_info()
