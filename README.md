# NutriApp

<img src="https://github.com/putuwaw/nutriapp/blob/main/static/images/logo.png" width="150px;" alt=""/>

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Forks](https://img.shields.io/github/forks/putuwaw/nutriapp?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/putuwaw/nutriapp?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/putuwaw/nutriapp?style=for-the-badge)

NutriApp is a website based application that able to select the foods with the highest protein content using Best-First Branch-and-Bound Algorithm.

## Features💡
By using NutriApp you can:
- [x] Get the image of the Space State Tree from the results of the best-first branch-and-bound algorithm.
- [x] Get information about which foods to eat to get the highest protein content.
- [x] Get information about the highest amount of protein that can be obtained.
- [x] Get information about the program running time.

## Technology 👨‍💻
NutriApp is created using:
- [Python](https://www.python.org/) - Python as the main programming language.
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Flask is a web framework for Python, based on the Werkzeug toolkit.
- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a front-end framework that allows for the creation of easy and responsive web layouts.
- [Vercel](https://vercel.com/) - Vercel is a cloud platform that we use to deploy our apps.
- [Docker](https://www.docker.com/) - Docker is a platform for developing, shipping, and running our applications.


## Structure 📂
```
NutriApp
├── .github
├── handlers
├── modules
├── static
│   ├── images
│   ├── scripts
│   └── styles
├── templates
├── tests
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── requirements.txt
└── vercel.json
```
- [.github](.github/) is a folder that used to place Github related stuff, like issue template and CI pipeline.
- [handlers](handlers/) contain handler to handling HTTP request methods, especially POST method.
- [modules](modules/) contain the main modules for implement the best-first branch-and-bound algorithm.
- [static](static/) contain static files like images, CSS, and JavaScript files.
- [templates](templates/) contain the file that will be rendered for display in the browser.
- [tests](tests/) contain unit test to make sure the main module work properly.
- [.gitignore](.gitignore) is a file to exclude some folders like venv.
- [Dockerfile](Dockerfile) is a file that contains all the commands to build an image.
- [LICENSE](LICENSE) is a file that contains the license we use in this app.
- [README.md](README.md) is the file you are reading now.
- [app.py](app.py) is the main file of this app.
- [requirements.txt](requirements.txt) is a file that contains a list of dependencies used in this app.
- [vercel.json](vercel.json) is a file that contains configuration and override the default behavior of Vercel.

## Requirements 📦
- Python 3.10 or later
- Bootstrap v5.2 or later
- Docker 20.10.17 or later

## Installation 🛠️
- Install Docker.
- Pull the image from [Docker Hub](https://hub.docker.com/r/putuwaw/nutriapp):
```
docker pull putuwaw/nutriapp
```
- Run the downloaded image:
```
docker run -p 8000:8000 putuwaw/nutriapp
```
- Open web browser and visit:
```
localhost:8000
```

## Contributors ✨
<br>
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/putuwaw"><img src="https://avatars.githubusercontent.com/u/90038606?v=4" width="150px;" alt=""/><br><sub><b>Putu Widyantara</b></sub></td> 
    <td align="center"><a href="https://github.com/putrip3"><img src="https://avatars.githubusercontent.com/u/103046943?v=4" width="150px;" alt=""/><br><sub><b>Putri Pratiwi</b></sub></td> 
    <td align="center"><a href="https://github.com/Kebelll"><img src="https://avatars.githubusercontent.com/u/97933526?v=4" width="150px;" alt=""/><br><sub><b>Kenny Belle</b></sub></td>
    <td align="center"><a href="https://github.com/madya-dev"><img src="https://avatars.githubusercontent.com/u/84718700?v=4" width="150px;" alt=""/><br><sub><b>Madya Santosa</b></sub></td>
  </tr>
</table>
