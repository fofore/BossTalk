from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import time

app = Flask(__name__)
# 프론트엔드(HTML)에서 서버로 접근할 수 있도록 허용
CORS(app)

# 업로드된 이미지를 임시 저장할 폴더 설정
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/try-on', methods=['POST'])
def virtual_try_on():
    # 1. 프론트엔드에서 보낸 사진 받기
    if 'person' not in request.files or 'garment' not in request.files:
        return jsonify({"error": "이미지가 누락되었습니다."}), 400

    person_file = request.files['person']
    garment_file = request.files['garment']

    # (옵션) 서버에 이미지 임시 저장
    person_path = os.path.join(UPLOAD_FOLDER, person_file.filename)
    garment_path = os.path.join(UPLOAD_FOLDER, garment_file.filename)
    person_file.save(person_path)
    garment_file.save(garment_path)

    # ---------------------------------------------------------
    # 🚨 여기에 실제 AI 모델 처리 로직이 들어갑니다! 🚨
    # 예: Replicate API 호출, IDM-VTON, OOTDiffusion 모델 실행 등
    # 지금은 테스트를 위해 3초 대기 후 임시 이미지를 반환합니다.
    # ---------------------------------------------------------
    
    print("AI 합성 진행 중...")
    time.sleep(3) # AI 처리 시간이라고 가정 (3초 대기)

    # 임시 결과 이미지 URL (실제로는 AI가 생성한 이미지의 경로를 반환해야 함)
    # 여기서는 샘플로 무료 이미지 URL을 반환합니다.
    dummy_result_image_url = "https://via.placeholder.com/400x500.png?text=AI+Generated+Fitting+Result"

    # 3. 완성된 이미지 주소를 프론트엔드로 다시 보내기
    return jsonify({
        "message": "success",
        "result_url": dummy_result_image_url
    })

if __name__ == '__main__':
    # 서버 실행 (포트 5000)
    app.run(debug=True, port=5000)
