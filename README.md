# HAAK - Helpful Automated Assistant for Kitchens (HAAK)
HAAK is a chatbot-like service that provides users with personalized dining options based on their location, time of day, and previous dining experiences. The system will use speech-to-text and direct text input to aid in user interactions and provide users relevant information in a simple and digestible format.

## Authors:
Carter Garcia \
Aasim Syed \
Jorge Bautista \
Jiangshan Ai \
Kerwin Lin

## Development Setup

<ol>
<li><code>git clone https://github.com/HAAK/HAAK</code></li>
<li>Install PostgreSQL and Flask.</li>
<li>Install Python 3.11.</li>
<li>Install pip using <code>python -m ensurepip</code></li>
<li>Using <code>pip</code> install the following packages:
<ul>
<li><code>yelpapi</code></li>
<li><code>ics</code></li>
<li><code>nltk</code></li>
<li><code>opencage</code></li>
</ul>
</li>
</ol>

## Environment Variables

The following are environment variables for the build.
```.env
POSTGRES_DATABASE=
POSTGRES_HOST=
POSTGRES_USERNAME=
POSTGRES_PASSWORD=
POSTGRES_PORT=
YELP_TOKEN=
OPENCAGE_TOKEN=
```