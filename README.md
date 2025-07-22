

export GITLAB_URL=<url>
export GITLAB_TOKEN=<token>
export GITLAB_PROJECT_ID=<id>


python main.py --input-path SQuIRRL.uml --output-path tmp/SQuIRRL.uml


docker image

$ docker build -t frittenburger/loadmodelfromgitlab:dev .