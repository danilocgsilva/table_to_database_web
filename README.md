# Table to database (web)

Fills a relational database wirh a xls file content.

## Usage

First, build the environment:
```
docker compose up -d --build
```
Then, for convenience, make the `start_server` executable and run it:
```
chmod +x start_server.sh
./start_server
```
Then, you can see the application in `http://localhost:5000`

**Note**: This docker receipt is suposedly to be serve a *development server*.
