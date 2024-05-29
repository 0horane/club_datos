import asyncio
import telegram
import selenium
import env

options = selenium.webdriver.ChromeOptions() 
options.add_extension('./vimium-c.crx')
options.add_argument('--disable-blink-features=AutomationControlled')
driver = selenium.webdriver.Chrome(chrome_options=options)

async def main():
    bot = telegram.Bot(env.TELEGRAM_TOKEN)
    async with bot:
        print(await bot.get_me())

if __name__ == '__main__':
    asyncio.run(main())

# driver.get