# LinkedIn <img src="https://img.icons8.com/fluent/48/000000/linkedin.png"/> Data Analytics using PowerBI  and Plotly :bar_chart: 

## Live Web-Application available [here.](https://linkedin-plotly-webapp.herokuapp.com/)

### Troubleshooting:
* If the live webapp fails to load and gives an ***Application Error***, then try refreshing the URL.

## Getting the Data:

### Step 1:
![1](https://user-images.githubusercontent.com/29462447/97801422-98bfa000-1c62-11eb-9e38-58dc6038f0b6.png)

### Step 2:
![2](https://user-images.githubusercontent.com/29462447/97801415-94938280-1c62-11eb-9e47-03396d196297.png)

### Step 3:
![3](https://user-images.githubusercontent.com/29462447/97801420-98270980-1c62-11eb-8ddc-5c05a0dd1f00.png)

## Installation:
Simply run ***pip install -r requirements.txt*** to install the necessary dependencies.

## Usage:
1. Navigate to the directory where you have cloned this entire branch contents.
2. Run the command: ***python app.py*** and your webapp will load in your default browser.

## Final Plotly Webapp would look like this in your favourite web-browser :wink: : 
<kbd>
<img src="https://user-images.githubusercontent.com/29462447/103694388-e89f4800-4fc0-11eb-9857-56300b93f7ed.png" data-canonical-src="https://user-images.githubusercontent.com/29462447/103694388-e89f4800-4fc0-11eb-9857-56300b93f7ed.png"/> 
</kbd>

## Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
4. Edit ***app.py*** by changing line 240 from **app.run_server(debug=True)** to **app.run_server(host='0.0.0.0',debug=True)**.
5. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build --tag linkedlin_app .
```
4. Run the docker:
```
docker run --publish 8000:8080 --detach --name app linkedlin_app
```

This will launch the dockerized app. Navigate to ***localhost:8000*** in your browser to have a look at your web application. You can check the status of your all available running dockers by:
```
docker ps
```

