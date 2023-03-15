import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="davinci:ft-personal-2023-02-10-06-40-47",
            prompt=generate_prompt(animal),
            temperature=0,
            max_tokens=128,
        )
        for choice in response.choices:
            print(choice)
        # return redirect(url_for("index", result=response.choices[0].text.rsplit("\\n")[0]))
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    prompt = animal + " ->"
    print(prompt)
    return prompt
