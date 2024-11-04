# SEO Blog Generator

Automatically generate SEO-optimized blog posts from RSS feeds using OpenAI's GPT-4.

## Features

- RSS feed processing
- SEO optimization using GPT-4
- Keyword research and analysis
- Content generation
- HTML and JSON output
- WordPress integration (optional)

## Prerequisites

- Python 3.8+
- OpenAI API key
- RSS feed URL
- WordPress credentials (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/seo-blog-automation.git
cd seo-blog-automation
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with your credentials:
```env
OPENAI_API_KEY=your-openai-api-key
WORDPRESS_URL=your-wordpress-url
WORDPRESS_USER=your-wordpress-username
WORDPRESS_APP_PASSWORD=your-wordpress-app-password
```

## Usage

1. Basic usage:
```bash
python main.py
```

2. Using Make commands:
```bash
make run    # Run the generator
make clean  # Clean output directory
make setup  # Initial setup
```

## Directory Structure

```
seo-blog-automation/
├── main.py                # Main script
├── requirements.txt       # Project dependencies
├── Makefile              # Make commands
├── run_seo.sh            # Shell script for automation
├── src/                  # Source code
│   ├── generators/       # Generation logic
│   └── utils/           # Utility functions
└── output/              # Generated content
    ├── blogs/          # Blog posts
    └── logs/           # Log files
```

## Configuration

Modify `config/settings.py` to adjust:
- OpenAI parameters
- Content generation settings
- SEO optimization rules
- Output formats

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/seo-blog-automation](https://github.com/yourusername/seo-blog-automation)

## Acknowledgments

- OpenAI GPT-4
- feedparser
- python-dotenv# seo-blog-automation
