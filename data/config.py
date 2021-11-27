from environs import Env


env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')

yookassa_test_token = env('YOOKASSA_TEST_TOKEN')
