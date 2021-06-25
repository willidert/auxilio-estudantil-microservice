FROM node:14.17-alpine

WORKDIR /app

COPY package-lock.json .

COPY package.json .

RUN npm install

RUN npm install -g @angular/cli

COPY . /app

EXPOSE 4200

CMD ["npm", "start"]
