# Property Search AI Enhancement

## Description

Imagine that:

* You come across a dreamy house but you cannot find it online.
* You have one photo and you want to search exactly with it.
* You want to find the property with some features.

We want to enhance the search function on main page, allowing our users to find the property they want based on the description of appearance with only  **a few words** or simply one **photo**.

What we gonna do is to set up a neural search engine using one multi-mode pre-trained model [*CLIP*](https://openai.com/blog/clip/). We encode the images of the properties and search the best fit property with one sentence or photo.

## Get Started

### 1. Environment

make sure that:

> python version >= 3.7.0

then:

```shell
pip install -r requirements.txt
```

### 2. Set up the server

You can run the server locally with the command below:

```shell
python -m clip_server ./server/search_flow.yml
```

Or we provide one dockerfile and you can build with that:

```shell
docker build -t ps-clip-server -f ./server/server.Dockerfile ./server/

docker run --name <Your Name> -p 61000:61000 ps-clip-server
```

### 3. Try the client

#### Run the jupyter notebook locally

You can try the client with jupyter notebook

```Shell
pip install -U jupyter
jupyter notebook
```

And open the file `client.ipynb` on jupyter notebook.

#### Or you can Run the BFF

```Shell
python -m flask --app bff_server run -p <YOUR_PORT>
```

API:

```
<host>:<port>/search?key=<SEARCH_WORD>&limit=<RESULT_LIMIT>
```
