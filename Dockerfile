FROM node:carbon-slim

# Create app directory
WORKDIR /crowstream_api

# Install app dependencies
COPY package.json /crowstream_api/
RUN npm install

# Bundle app source
COPY . /crowstream_api/
RUN npm run prepublish

CMD [ "npm", "run", "runServer" ]