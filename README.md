# The Idea:
This repo is just an experiment to see if I can get a LLM to train another LLM much like how the [Alpaca model](https://crfm.stanford.edu/2023/03/13/alpaca.html) was trained at Stanford. However, I want to do it without fancy GPUs.

# To get started:
After cloning the repo, set up a virtual environment with pipenv and python 3.11

```bash
pipenv --python 3.11
```

After starting your shell, install the dependencies with pipenv

```bash
pipenv shell
```

```bash
pipenv install
```


You must store the path to your model in `models` directory, unless you want don't use the default

A GPU is not necessary to use this thanks to the great folks over at [llama.cpp](https://github.com/ggerganov/llama.cpp). You will need to install llama-cpp-python, however.


