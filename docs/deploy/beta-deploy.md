# Beta Deployment Guide (Railway + Vercel)

## 왜 이전 스캐폴드에서 개선했는가
- 컨테이너 시작 시 매번 `pip install` / `npm install` 하던 흐름을 제거하고, Docker build 단계에서 의존성을 고정 설치하도록 개선했습니다.
- worker/scheduler 주기를 환경변수로 제어할 수 있게 바꿨습니다.

## 1) API/Worker/Scheduler 배포 (Railway)
1. Railway 프로젝트 생성 후 `apps/api`를 서비스 루트로 지정.
2. API 서비스 시작 명령: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
3. Worker 서비스 시작 명령: `python -m app.workers.runner`
4. Scheduler 서비스 시작 명령: `python -m app.workers.scheduler`
5. Postgres/Redis 플러그인 추가 후 환경변수 연결:
   - `DATABASE_URL`
   - `REDIS_URL`
   - `PYTHONPATH=/app`

## 2) Web 배포 (Vercel)
1. Vercel 프로젝트에서 루트를 `apps/web`로 설정.
2. Build command: `npm run build`
3. Runtime command: `npm run start -- -p 3000`
4. 환경변수:
   - `NEXT_PUBLIC_API_BASE_URL=https://<railway-api-domain>/api/v1`

## 3) 배포 확인
- API: `GET https://<railway-api-domain>/health` → `{"status":"ok"}`
- Web: `https://<vercel-domain>` 첫 화면 확인

## 4) 베타 URL 전달 템플릿
- Frontend URL: `https://<vercel-domain>`
- Backend URL: `https://<railway-api-domain>`
