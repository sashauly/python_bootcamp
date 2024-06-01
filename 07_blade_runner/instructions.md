# Day 07: Blade Runner

## ex00

Is this testing whether I'm a replicant, or a lesbian, Mr Deckard?
Anyway, you can run the Voight-Kampff test with:

```bash
python main.py questions.json
```

## ex01

Basically there are unit tests for major edge cases. You can run them with:

```bash
python -m unittest -v tests.test_main
```

## ex02

basically, i only installed sphinx and ran the following command:

```bash
sphinx-quickstart docs
```

then in docs/source/index.rst i added info about functions and classes and ran the following command:

```bash
make html
```

then i opened the index.html file in the docs folder.

basically you only need to `cd docs` and run `make html` in the terminal.
