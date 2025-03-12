# Use official Node.js image
FROM --platform=linux/amd64 node:20

WORKDIR /app

COPY package.json .

COPY package-lock.json .
# force install on dependencies
RUN npm install --force  

COPY . .

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]