import React from 'react';
import NavScrollExample from '../Navbar/Navbar';
import './Location.css';  // Import a separate CSS file for styling

function Location() {
    return (
        <>
            <NavScrollExample />
            <div className="location-container">
            
            <iframe
            // eslint-disable-next-line
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3807.650282912087!2d78.38013327485646!3d17.380553183505448!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb942a2497f349%3A0x5c30ca8d2ffb8734!2sVasavi%20College%20of%20Engineering!5e0!3m2!1sen!2sin!4v1700844383908!5m2!1sen!2sin"
                width="600"
                height="450"
                style={{ border: "0" }}
                allowFullScreen=""
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
            ></iframe>
        </div>
        </>
    );
}

export default Location;
