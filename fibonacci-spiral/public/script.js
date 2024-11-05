// public/script.js
document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('fibonacci-container');
    const zoomInButton = document.getElementById('zoom-in');
    const zoomOutButton = document.getElementById('zoom-out');

    let fibPrev = 0;
    let fibCurrent = 1;
    let angle = 0; // Angle in degrees for spiral
    let radiusIncrement = 20; // Initial distance from the center for each Fibonacci number
    let zoomLevel = 1; // Initial zoom level

    // Function to add a Fibonacci element to the spiral
    function addFibonacciElement() {
        const newElement = document.createElement('div');
        newElement.className = 'spiral-element';
        newElement.textContent = `${fibCurrent}`;

        // Calculate position for spiral placement relative to the center of the viewport
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2;

        // Use zoom level to calculate position
        const x = centerX + Math.cos(angle * (Math.PI / 180)) * (radiusIncrement * zoomLevel);
        const y = centerY + Math.sin(angle * (Math.PI / 180)) * (radiusIncrement * zoomLevel);

        // Set the calculated position
        newElement.style.left = `${x}px`;
        newElement.style.top = `${y}px`;

        // Append to container
        container.appendChild(newElement);
        console.log(`Added: ${fibCurrent} at (${x}, ${y})`); // Log position

        // Update for the next Fibonacci number
        const nextFib = fibPrev + fibCurrent;
        fibPrev = fibCurrent;
        fibCurrent = nextFib;

        // Increase the angle and radius for the spiral effect
        angle += 30; // Increase angle for next position
        radiusIncrement += 5; // Increment radius for spacing
    }

    // Add the first Fibonacci element
    addFibonacciElement();

    // Infinite scroll event listener
    window.addEventListener('scroll', function () {
        addFibonacciElement(); // Add a new Fibonacci element when scrolling
    });

    // Zoom In functionality
    zoomInButton.addEventListener('click', function () {
        zoomLevel *= 1.2; // Increase zoom level
        container.style.transform = `scale(${zoomLevel})`; // Apply zoom
    });

    // Zoom Out functionality
    zoomOutButton.addEventListener('click', function () {
        zoomLevel *= 0.8; // Decrease zoom level
        container.style.transform = `scale(${zoomLevel})`; // Apply zoom
    });
});
