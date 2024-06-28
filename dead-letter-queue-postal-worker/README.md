# dead-letter-queue-postal-worker
![context-logo](readme/postal-worker.png)

# The postal worker takes care for the dead letters in the dlqs


## architecture

``` plantuml
!include architecture.iuml
```

## program sequence

``` plantuml
!include program_sequence.iuml
```

### Package main
This is the main package of the program and the starting point. It coordinates the program flow and calls other packages, like logfile analysis, as needed.
Central properties are placed in a central property file. 

### Package activemq
The activemq package helps to handle dead letter queues (DLQs) and their messages.
The contained messages could not be sent to their destination, so they are placed into the DLQ.
The activemq package take over the message handling. A suitable operation for those messages could be:

#### Message handling 
##### 'Retry' message
A retry puts the message into the former message queue from where the message came from.
In that queue the message is processed again. That is a good step for temporary issues inside the process.
#### 'Delete' message
If a message could not be handled by retrying, there are reasons for that. The issue has to be solved before
a message could be handled successfully. But if there is no change to solve the issue, the message could be cleaned
by delete.
#### Configure properties
Set required properties inside 'properties.py'.
Use 'properties-template.py' as an example.

### Package centraljira
The centraljira package enables you to administrate dlq-tickets. It can create and update existing dlq-tickets.

#### Create dlq-ticket
The creation can be triggered by calling the separate create-script and hand over specific parameters.
These parameters were used to fill the dlq-ticket.

Use the following command to call the script:
'cd [path-to-repository]/centraljira && /usr/bin/poetry run python create_ticket.py [NOT_USED_PARAMETER] [SUMMARY] [TICKET_DESCRIPTION] [LABEL]'

automatic field values:
- assignee : current user login
- priority : ASAP
- project  : ESB

##### Create dlq-ticket from nagstamon
The python script can be called from nagstamon. You can use the existing variables set by nagstamon to dynamically fill the parameter's values:
'cd [path-to-repository]/centraljira && /usr/bin/poetry run python create_ticket.py "$HOST$" "$SERVICE$" "$STATUS-INFO$" "DLQ"'

#### Update dlq-ticket
The ticket update can be used by another python module and can hand over parameters as well.

## Quick Start
### Requirements
- Docker and docker-compose installed
- Python and Poetry installed
- Access to Git repository
- git access token for your (personal) account
- Jira login token
### Setup
- check out repository
  - enter repository and go to subfolder dead-letter-queue-postal-worker
- configure property file
  - add activeMQ endpoints and credentials 
  - add Jira endpoint and credentials 
### Build constainer
- docker-compose build --build-arg username=[git-username] --build-arg password=[git-token] --no-cache

Notice:
- User and token might be stored in your command history, so you better clear it afterward.
- While the terminal echos the output of the build process the compose-command is displayed with a rendered username and token, 
so be sure nobody is watching your terminal. 

### Start container
- start the container and execute a run with the command 'docker-compose up -d'
- check logfile / ticket for results

## Development
### Requirements
- IDE
- python > 3.10
- poetry
### Setup
- check out repo and load into IDE
- create {project-path]/.venv
- in the projekt directory execute 'poetry install' to install the python dependencies into the .env dir
- configure IDE
  - add module dedicated SDK
    - virtual env
      - set to .venv created before
- install browser dependencies in playwright
- playwright install firefox --with-deps --force

