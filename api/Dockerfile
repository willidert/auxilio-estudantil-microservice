FROM node:14.17-alpine

# Create work directory
WORKDIR /app

# Copy dependencies
COPY package-lock.json .

COPY package.json .

RUN npm install

COPY . /app

EXPOSE 3333

RUN chmod +x wait-for-it.sh

# Build and run the app
CMD ["npm", "start"]
