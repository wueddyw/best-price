import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [url, setUrl] = useState('');
    const [item, setItem] = useState(null);
    const [loading, setLoading] = useState(false);
    const [hasAttemptedFetch, setHasAttemptedFetch] = useState(false);

    const handleSubmit = async () => {
        setLoading(true);
        setHasAttemptedFetch(true);
        setItem(null); // Reset item state before fetching
        try {
            const response = await axios.post('http://localhost:5000/scrape', { url });
            if (response.data.title === 'Title not available' && response.data.price === 'Price not available') {
                setItem(null); // No valid data found
            } else {
                setItem(response.data); // Set the scraped item data
            }
        } catch (error) {
            console.error('Error fetching data', error);
            setItem(null); // Error case, consider no valid data
        }
        setLoading(false);
    };

    return (
        <div>
            <h1>Find the Cheapest Item</h1>
            <input
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Enter URL"
            />
            <button onClick={handleSubmit} disabled={loading}>
                {loading ? 'Scraping...' : 'Scrape'}
            </button>
            <div>
                {loading ? (
                    <p>Loading...</p>
                ) : hasAttemptedFetch ? (
                    item ? (
                        <div>
                            <h2>{item.title}</h2>
                            <p>Price: {item.price}</p>
                        </div>
                    ) : (
                        <p>No items found</p>
                    )
                ) : null}
            </div>
        </div>
    );
}

export default App;
