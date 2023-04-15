from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "25281981")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "b2787e463962d1eb306bb0608a188a83 تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "6211334508:AAFvE9cTSif_G9Ep-e3OcAYd5JBV3fy9YMo")
SESSION_NAME = getenv("SESSION_NAME", "BAGBxb0AhnkWT58xAiacTmOV-FJx0xqqOHyHcHxCaASdrbJ4Dn26XqllVISrFoG1I3NK8tBM7hw1PHG-HfPLKQ9nf9nsqQbZUdoedgHOjiKA006SNZW797klgFloULoxLQid3WJPyMSYsyzQTIBTj6aoFAzHxDZc77gE5ZRQ3PXtEdhZZaZXLLcaGGHRslHeflSTqTsj22QltpZqMEJws873PjR4-_ztRSB9D1wZ7Erj6g0aJqV_SuHFmqZb1ARZkGgla5KLrlYgZAwTclcscpWKFLDkcTpXgnWwk5wwhkTRM1IXoaWsvmjKlNSoYZn7rVysqQ5hpRR_Q9EX6YxJCmdLr8nGFwAAAAFshVwtAA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Emre_kabasakal") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "love_music") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "Snow_White1_Bot") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Love00chaT") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "WWWROROO") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1921025470").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1921025470").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
