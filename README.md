# DevOps Core Practical Project



## The Brief
Below is my implementation of the SFIA Devops Core Practical Project. In this project, my task is to create an application composed of a service-oriented architecture which runs 4 APIs as different services. The core service, and the frontend is Service 1, and it is responsible for communicating with the three others. Services 2 and 3 will act as random object generators, and service four will combine their results and this will be presented to the user on the front end. The application must run as a CD pipeline making use of containerisation, a CI server and an orchestration tool. And the app must run via a reverse proxy as a load balancer.

### Additional Requirements
Additionally the project requires the following:
* A Kanban board
* A simple relational database for data persistence
* Clear documentation of design, architecture, pipeline and risk assessment


### My Implementation - A Stock predicting App
To achieve the above aims, I have chosen a simple stock prediction app that allows the user to:
* Choose a stock ticker
* Post it to three backend services:
    * Backend1 calculates a prediction of the stock return and sends it to the frontend
    * Backend2 calculates a random value as a prediction from the ticker price and standard deviation
    * Backend3 returns a string showing the two values calculated from backend1 and backend2 along with the original stock price of the ticker and its return
* The interface is a simple frontend with two html web pages

## Architecture
### Database structure
Pictured below is the simple entity diagram (ED) showing the structure of the database.
As can be seen it is a very simple table with two rows, the id row and the final_result row which persists the final front end display.

![ed][ed]

### Service diagram
Pictured below are the existing services in the app and how they communicate with each other.

![services][services]

As can be seen, the frontend application is the user facing service. Here the user puts in the ticker. It is then sent to the backend1, which makes an external api call and then performs either an ARIMA or SARIMAX prediction on the collected stock prices from the api. The standard deviation, current and immediate previous prices are also collected. These are sent to the frontend api. It sends the current price and standard deviation to the backend2, which calcuates a random number within the range of the standard deviation around the current price. This value is sent back to the frontend as a prediction. The two predictions are then sent back to backend3 along with the current price and previous price. These are used to generate a final message that is sent to the frontend, persisted in the database and exposed on the html using Jinja2. 

### Continous Delivery (CD) Pipeline
The diagram below shows the CD pipeline with the associated frameworks and services responsible for each stage. The pipline is automating the deployment process from the point of pushing my code onto github through to building images and containers for the app using docker, to configuring the virtual machines hosting the app, through to deploying the app accross these machines behind an nginx load balancer. The initial automation is done by webhook connected to github from jenkins, and then pushed through the CI pipeline on Jenkins.
Tests are automatically run and reports are produced at each stage. The design of this job means that if a build on one stage fails, the job wll fail to build and I will be notified as to this with logs provided to pinpoint where the problem is.

![ci][ci]

The build stages are listed below:
* Checkout (Pull code from the repository)
* Test
* Build and Push Images
* Configuration Management
* Deployment

![buildstages][buildstages]

## Project Tracking
The kanban board used for project tracking was Trello. A link to the board can be found here:

![trello1][trello1]

Above is the initial kanban board at the start of the project

![trello2][trello2]

Above is the final kanban board. The elements of the project move from lwft to right.


## Risk Assessment
Below is the initial risk assessment for the project. A link can be found here:


![risk1][risk1]

Below is the final risk assessment:

![risk2][risk2]

## Testing
pytest is used for all testing in the project. The testing achieved high coverage due to the simplicity of the app as can be seen in the diagrams below.

![testResult1][testResult1]

![testResult2][testResult2]

![testResult3][testResult3]

![testResult4][testResult4]


![coverage][coverage]


## Frontend

The app has a simple design as can be seen below. You are instructed to input a ticker and the prediction information appears below.

![frontend1][frontend1]

You can also see the last five predictions at the click of a botton:

![frontend2][frontend2]

## Future Improvements

For the future, this app can be highly improved. A form in the homepage would make the app more interactive and allow for more information to be requested about the ticker. This would mean linking to more apis calls. The overall appearance of the app could be greatluy improved. The predictions could be more robust as opposed to using a simple ARIMA model from statstools.

## Authors
* Ope Orekoya


[ed]: https://imgur.com/9J7aspH.png
[services]: https://imgur.com/QGzEJ2d.png
[ci]: https://imgur.com/jmBbWLj.jpg
[buildstages]: https://imgur.com/y7ZVbkW.png
[trello1]: https://imgur.com/TKwuhdX.png
[trello2]: https://imgur.com/jNBU1He.png
[risk1]: https://imgur.com/TVPGIXH.png
[risk2]: https://imgur.com/C2DUvj7.png
[testresult1]: https://imgur.com/9b4xkXl.png
[testresult2]: https://imgur.com/gqhzNRz.png
[testresult3]: https://imgur.com/J6r9aFa.png
[testresult4]: https://imgur.com/NbfSt3W.png
[coverage]: https://imgur.com/bmf58DR.png
[frontend1]: https://imgur.com/hj0fArU.png
[frontend2]: https://imgur.com/PkAxZA5.png
