# Stack
- Python 3.8
- Django 3.1
- Postgres 12

# Prerequisites
 - Docker
 - Docker-compose

# Runserver
- `chmod +x ./scripts/wait-for-it.sh`
- `chmod +x ./scripts/wait-for-postgres.sh`
- `bash run-server` or `mux .` (if you have tmux and tmuxinator)

# Deployment
TODO

# backend shell
`docker run -it --expose 8000 -w /opt/app -v $(pwd)/django:/opt/app python:3.8-alpine sh`

# frontend shell
`docker run -it --expose 4200 -w /opt/app -v $(pwd)/angular:/opt/app node:12.18.1-alpine sh`
