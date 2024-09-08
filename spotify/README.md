# Spotify Data Scraper

This repository contains a Python script that scrapes data from the Spotify API to collect and analyze information on Nigerian Afrobeats artists. The goal is to use the data to track artist popularity, followers, and collaboration networks, which can provide valuable insights into the Afrobeats music industry.

## Features

- Collects detailed data on top Afrobeats artists, including:
  - Artist Name
  - Artist ID
  - Popularity Score
  - Total Followers
- Exports the data into a structured JSON format for further analysis.
- Uses Spotify's public API to fetch real-time data about the artists.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Example Output](#example-output)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

Follow these steps to set up and run the scraper on your local machine.

### Prerequisites

- Python 3.8 or higher
- Spotify Developer Account (for API credentials)
- The following Python packages:
  - `requests`
  - `python-dotenv`

### Step 1: Clone the Repository

```bash
git clone https://github.com/denironyx/scraper.git
cd scraper/spotify
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
- Create a .env file in the root of the spotify folder.
- Add your Spotify API credentials (CLIENT_ID and CLIENT_SECRET) to the .env file:
```bash
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
```
You can obtain these credentials by signing up for a Spotify Developer account at https://developer.spotify.com/.

### Usage
To run the scraper and collect data on Nigerian Afrobeats artists:

Ensure that your .env file is set up with your Spotify credentials.
Run the script:

```
python fetch_nigeria_artists_data.py
```

The script will fetch data on a predefined list of Afrobeats artists and store the data in a nigerian_artists_data.json file.

#### Customizing the Artist List
The list of Afrobeats artists is predefined in the scraper.py file, but you can modify or add to the list as needed:

```
afrobeats_artists = [
    "Davido",
    "Wizkid",
    "Burna Boy",
    "Asake",
    "Tiwa Savage",
    ...
]
```
### Configuration
- API Token: The script retrieves a Spotify API token using your CLIENT_ID and CLIENT_SECRET. You can modify the get_token() function if needed.
- Artist Query: The search_for_artist() function performs a search query for each artist, fetching relevant data like popularity and follower count.

### Example Output
After running the script, a JSON file named nigerian_artists_data.json will be generated. Here is an example of the output:

```
[
    {
        "artist_name": "Davido",
        "artist_id": "0Y3agQaa6g2r0YmHPOO9rh",
        "popularity": 85,
        "followers": 1200000
    },
    {
        "artist_name": "Wizkid",
        "artist_id": "3HXkGoawzSOBVl9Ltg69Hd",
        "popularity": 90,
        "followers": 1500000
    }
]

```
### Contributing
Contributions are welcome! Feel free to open a pull request or issue if you have suggestions for improvements or find any bugs. Please ensure that your changes include relevant tests.