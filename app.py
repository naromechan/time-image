from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import io

app = Flask(__name__)

@app.route("/")
def generate_image():
    now = datetime.now().strftime("%H시")

    img = Image.open("base.png").convert("RGB")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    draw.rectangle((100, 400, 500, 520), fill=(0,0,0))
    draw.text((120, 410), f"{now}라니……", font=font, fill=(230,230,230))

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype="image/png")

app.run(host="0.0.0.0", port=5000)
