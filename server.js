const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3000;

// 프론트엔드에서 API를 호출할 수 있도록 CORS 허용
app.use(cors());
// POST 요청 시 JSON 데이터를 읽기 위한 설정
app.use(express.json());

// 임시 데이터베이스 (실제로는 MySQL, PostgreSQL 등을 연결합니다)
const db = {
    posts: [
        { id: 1, region: "경기 용인시", category: "프리미엄 만화카페", title: "닌텐도 스위치 조이콘 수리 어디서 하시나요?", author: "익명", time: "2026-03-06T10:00:00Z" },
        { id: 2, region: "경기 용인시", category: "보드게임 카페", title: "신작 보드게임 추천 좀 부탁드립니다.", author: "주사위굴려", time: "2026-03-06T09:00:00Z" },
        { id: 3, region: "서울 강남구", category: "세무/노무", title: "5월 종소세 신고 관련 질문있습니다.", author: "강남초보", time: "2026-03-05T15:00:00Z" }
    ]
};

// [소통방 API] 게시글 목록 조회 (필터링 포함)
app.get('/api/community/posts', (req, res) => {
    const { region, category } = req.query; // URL에서 쿼리 파라미터 추출 (?region=...&category=...)
    
    let filteredPosts = db.posts;

    // 1. 지역 필터링
    if (region) {
        filteredPosts = filteredPosts.filter(post => post.region === region);
    }
    // 2. 업종 필터링
    if (category) {
        filteredPosts = filteredPosts.filter(post => post.category === category);
    }

    // 성공 응답 전송 (JSON 형식)
    res.status(200).json({
        status: "SUCCESS",
        count: filteredPosts.length,
        data: filteredPosts
    });
});

// 서버 실행
app.listen(PORT, () => {
    console.log(`사장톡 백엔드 서버가 http://localhost:${PORT} 에서 실행 중입니다.`);
});