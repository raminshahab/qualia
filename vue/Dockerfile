# Example Dockerfile for Vue
FROM node:18

WORKDIR /app

# Copy package files FIRST to leverage Docker caching
COPY package*.json ./

# Install dependencies (including vite)
RUN npm install

# Copy source code
COPY . .

# Run dev command
CMD ["npm", "run", "dev"]