# Current Status

## 기획/설계 진행 상태
- MVP 요구사항 정의 완료
- IA(대시보드/카테고리/상세/알림/설정) 정의 완료
- 온보딩 3단계 플로우 정의 완료
- 주간 요약 로직(점수 기반) 정의 완료
- 권한/동의 문구 초안 정의 완료

## 기술 설계 상태
- DB 스키마 초안 도출 완료
- API 엔드포인트 초안 도출 완료
- 컴포넌트 구조 초안 도출 완료

## 구현 초안 상태
- FastAPI 라우터 구조 초안
- Onboarding/Dashboard API 템플릿 초안
- Next.js 로그인/온보딩/대시보드 페이지 템플릿 초안
- JWT 인증 흐름 초안
- cookie 기반 인증 전환 가이드 초안

## 미완료/주의
- 실제 Instagram OAuth 연동 구현 필요
- Worker/Scheduler 실제 연결 필요
- DB 마이그레이션 및 FK/인덱스 확정 필요
- 개인정보 삭제 파이프라인 구현 필요
- 운영 보안설정(HTTPS, secure cookie, CORS 도메인 제한) 필요
