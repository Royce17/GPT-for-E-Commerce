import openai

response = openai.Completion.create(
            model="davinci:ft-personal-2023-02-10-06-40-47",
            prompt="对以下商品进行强烈地夸赞：彩妆中的防晒，卖点为防晒值是PA++++，能防晒黑。",
            temperature=0,
            max_tokens=128,
        )

print(response.choices[0].text.rsplit("\\n")[0])