# %% [markdown]
# # Property Search Demo

# %% [markdown]
# Add client here

# %%
from clip_client import Client
from docarray import Document, DocumentArray

client = Client('grpc://0.0.0.0:61000')

# %% [markdown]
# Load the images here

# %%
docs = DocumentArray.from_files('./images/*.jpg')
docs.plot_image_sprites()
docs

# %% [markdown]
# Encode the images

# %%
docs = client.encode(docs, show_progress=True)
docs.plot_image_sprites()
docs

# %% [markdown]
# Search with text

# %%
# result = client.search(["A house with red roof"], limit = 3)
# vec = client.encode(["red roof"])
vec = client.encode(["white house"])
result = docs.find(query=vec, limit = 1)
result

# %%
# print(result.index)
# print(result['@m', ['text', 'scores__cosine']])
result[0].plot_image_sprites()


