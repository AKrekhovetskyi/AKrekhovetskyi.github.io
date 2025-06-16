# TechTrendStatWeb

This repository contains the source code and content for [AKrekhovetskyi.github.io](https://akrekhovetskyi.github.io), a personal website and blog powered by [Jekyll](https://jekyllrb.com/) and the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme, deployed via GitHub Pages.

The data used in the posts of this project was collected by the [**TechTrendStat**](https://github.com/AKrekhovetskyi/tech-trend-stat) project.

## Features

- **Modern Jekyll Theme:** Uses the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme for a clean, responsive, and feature-rich blog.
- **Automated Posts:** Python scripts in [`post_maker/`](post_maker/) generate and update posts, statistics, and diagrams from data sources.
- **Job Listings:** Regularly updated job vacancy posts for Java, JavaScript, and Python in [`_posts/`](./_posts/).
- **Statistics & Diagrams:** Technology trends visualized in statistics posts, with diagrams stored in [`assets/diagrams/`](assets/diagrams/).
- **Custom Plugins:** Ruby plugins in [`_plugins/`](./_plugins/) extend Jekyll functionality (e.g., last modified date for posts).
- **Self-hosted Assets:** Static libraries managed in [`assets/lib/`](assets/lib/) for development and production.

## Directory Structure

```
.
├── _config.yml            # Jekyll configuration
├── _posts/                # Blog posts (vacancies & statistics)
│   ├── Java/
│   ├── JavaScript/
│   └── Python/
├── _plugins/              # Custom Jekyll plugins
├── _tabs/                 # Navigation tabs (About, Archives, etc.)
├── assets/                # Static assets (images, diagrams, libraries)
├── post_maker/            # Python scripts for post generation
├── index.html             # Home page
├── Gemfile                # Ruby dependencies
├── requirements.txt       # Python dependencies
└── tools/                 # Utility scripts (e.g., test.sh)
```

## Usage

### Local Development

1. **Install Ruby & Bundler:**
   ```sh
   gem install bundler
   ```

2. **Install dependencies:**
   ```sh
   bundle install
   ```

3. **Install Python dependencies (for post generation):**
   ```sh
   python3 -m venv .venv
   . .venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Clone submodules for static assets:**
   ```sh
   git submodule update --init --recursive
   ```

5. **Serve locally:**
   ```sh
   bundle exec jekyll serve
   ```

### Generating Posts

- Use the scripts in [`post_maker/`](post_maker/) to generate or update job vacancy and statistics posts.
- Example:  
  ```sh
  python3 -m post_maker.make_posts
  ```

### Testing

- Run the test script to build and check the site:
  ```sh
  bash tools/test.sh
  ```

## Deployment

- The site is automatically deployed via GitHub Pages on push to the `main` branch.
- Ensure submodules are updated in your GitHub Actions workflow if you self-host assets.

## Customization

- Edit `_config.yml` to adjust site settings.
- Add or modify posts in `_posts/`.
- Update navigation tabs in `_tabs/`.
- Customize plugins in `_plugins/`.

## License

This project is licensed under the [MIT License](LICENSE).

---

**References:**
- [Chirpy Theme Documentation](https://github.com/cotes2020/jekyll-theme-chirpy/wiki)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
