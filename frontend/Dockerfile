# Use the official Node.js image
FROM node:18

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json ./
RUN npm install

# Copy the project files
COPY . .

# Expose the port
EXPOSE 4200

# Run the Angular application
CMD ["npm", "start", "--host", "0.0.0.0" ]

