# Quotes Scraper

Quotes Scraper is a tool that automatically scrapes quotes from the http://quotes.toscrape.com/js-delayed/ website. It fetches quotes from all pages and saves them into a single JSON Lines file.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.7 or later.
* You have a `<Windows/Linux/Mac>` machine.

## Installing Quotes Scraper

To install Quotes Scraper, follow these steps:

Install requirements.txt:
```sh
pip install -r requirements.txt
```

Windows:
```cmd
py -m pip install -r requirements.txt
```

## Using Quotes Scraper

To use Quotes Scraper, follow these steps:

1. Create a virtual environment.

2. Create a .env file in the project's root directory with the following environment variables:

```sh
INPUT_URL=http://quotes.toscrape.com/js-delayed/
OUTPUT_FILE=output.json
```

3. Run the Python script:

```sh
python run.py
```

## Contributing to Quotes Scraper

To contribute to Quotes Scraper, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

## License

This project uses the following license: [MIT License](https://opensource.org/licenses/MIT).

## Contact

You can reach me at `maciej.brasewicz@gmail.com`.
