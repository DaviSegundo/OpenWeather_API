# Weather API Collector

## Project's goal
> This project was focused on building a service that collects data from a weather API and stores this information in a database. The beginning of the flow occurs when a user requests the beginning of a data collection, informing a unique identifier for it. This starts the collection of information and using the API that was built, the user can monitor the progress of their data collection.

## Basic architecture overview
The application flowchart was designed for the API to receive the user's request, save the basic information about the data in the database and send the request to start a new data collection to the broker, which will forward it to one of the workers. available that will start collecting the data. 
<p align='center'>
    <img src='./docs/IT services.png' height=400>
</p>
In this way, workers save the new data acquired in the database. In addition, a request can be sent to the API to find out how the data collection is progressing.

## Requirements
Tools and packages required to successfully install this project.
- Python 3.8: [Python Releases](https://www.python.org/downloads/)
- Docker: [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Tools used
#### Flask:
The choice of the **Flask** framework was due to the familiarity I already have with it, but not only that, the ease and robustness to make the necessary implementations. In addition, the **flask-restx** library was another important factor, as it made the construction of **Swagger** a lot easier, which is something of paramount importance to have in a project with an API.

#### MongoDB:
**MongoDB** was chosen due to the non-relational data structure, ie **NoSQL**, which in this context helps with the ease of manipulation of the structures that would be stored in it. In addition, it is one of the databases that I have used the most recently and personally I really like how it works and it also has a great **ORM** that helps a lot in the data manipulation part, providing a schematization for documents and a much more simplified way to carry out some queries.

#### RabbitMQ:
The choice to implement a broker in the project was due to the need for the requests to be **asynchronous**. So I opted for **RabbitMQ** as it provides an easy way to implement the basics and has excellent documentation. Thus, a **temporal decoupling** for the application flow and a way to organize data collection in a more logical way was achieved.

## Docker Installation
The idea of the project is to have the entire application in containers, so the services were placed in containers using Docker and a structure was prepared for their execution. Compose build and run files are available in the project.



### How to run
To run the project, follow the instructions below. It is worth remembering that due to the nature of the project, the API, database and broker services were allocated in docker-compose for easier startup. As we can have several workers, its execution command can be used to start new instances if necessary.

#### First step:
Access the directory where the docker-compose file is and run the following command. With this successful, the API, database and broker services will be started.
```sh
docker compose -f "docker-compose.yml" up -d --build
```
<p align='center'>
    <img src='./docs/docker_env.png'>
</p>

#### Second step:
After the previous services have started, it is now possible to allocate workers. Use the following in the terminal to allocate 1 worker. For each new instance it is possible to use a new terminal.
```sh
docker run -it --network=host davisegundo88/workerweather:main -h 127.0.0.1
```
<p align='center'>
    <img src='./docs/worker_terminal.png'>
</p>

#### Third step:
With all the services started, it is now possible to use all the features of the application. To access the API, go to **localhost:5000**, where you will find the Swagger interface and from there just perform the POST with a user identifier and monitor the data collection process through the GET route.

<p align='center'>
    <img src='./docs/request_success.png'>
</p>
<p align='center'>
    <img src='./docs/request_get_success.png'>
</p>