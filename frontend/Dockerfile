FROM node:20-alpine

WORKDIR /frontend

COPY package.json ./

COPY . .

RUN npm install -g npm@latest

RUN npm install --legacy-peer-deps

RUN npm run build

EXPOSE 5173

CMD ["npm","run", "dev"]

