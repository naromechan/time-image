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

    # ✅ 기본 폰트 (위치 확인용)
    font = ImageFont.load_default()

    # ✅ 좌표 (여기만 계속 수정)
    x, y = 330, 780

    # ✅ 빨간색으로 표시 (눈에 잘 보이게)
    draw.text((x, y), f"{now}라니……", font=font, fill=(255,0,0))

    # ✅ 이미지 반환
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype="image/png")

app.run(host="0.0.0.0", port=5000)
