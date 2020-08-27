# ビルド環境(distを作るためだけの仮の環境)
# lts:安定版・alpine:軽量
FROM node:lts-alpine as build-stage

ENV API_URL="http://localhost:8000/"

# /code生成も
WORKDIR /code

COPY ./package.json ./
RUN npm install
# 他のファイル群(/src, nuxt.config.jsは必須)
COPY ./ ./
# コンテナ内の/codeに/dist生成
RUN npm run generate && npm run build



# 本番環境
FROM nginx:stable-alpine as production-stage

# ビルド環境内で生成した/distをマウント
COPY --from=build-stage /code/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
