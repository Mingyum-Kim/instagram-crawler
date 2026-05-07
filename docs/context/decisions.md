# Product & Tech Decisions

## 제품 의사결정 (확정)
- 플랫폼: 웹 우선
- 타겟: 일반 사용자
- 정리 방식: 자동 분류 중심
- 알림 채널: 웹 내 알림
- 데이터 범위: 저장 게시물 + 저장 릴스 + 정보성 DM 텍스트
- 검색: MVP에서 제외 (자동 스캔/재노출 중심)
- 온보딩: 3단계 후 동기화 시작
- 권한: 동기화 전 필수 동의 확인
- 비즈니스: 무료 검증

## UX 방향
- 수집은 자동
- 정리는 자동
- 소비는 요약/카테고리/주간 리마인드 중심
- 사용자 수동 입력 최소화

## 기술 의사결정 (기본값)
- Frontend: Next.js
- Backend: FastAPI
- DB: PostgreSQL
- Queue/Cache: Redis
- Background jobs: Worker + Scheduler
- Auth: JWT 기반 (httpOnly cookie 권장)

## 보안/개인정보 원칙
- DM 텍스트는 서비스 목적 범위 내 분석
- 민감정보 마스킹
- 연동 해제/데이터 삭제 요청 지원
- 동의 이력(버전/시각) 저장
