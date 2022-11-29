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

```shell
python -m clip-server search_flow.yml
```

### 3. Try the client

You can try the client with jupyter notebook

```Shell
pip install -U jupyter
jupyter notebook
```

And open the file `client.ipynb` on jupyter notebook.
