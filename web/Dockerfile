# Build stage
FROM node:21 AS build

WORKDIR /app

COPY package.json package.json
RUN npm install

COPY . .
RUN npm run build

# Production stage
FROM nginx:1.19

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]