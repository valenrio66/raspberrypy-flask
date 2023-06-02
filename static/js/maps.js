// Create a map instance
const map = L.map("map").setView(
	[-6.914008105946337, 107.619119593642],
	23
);

// Add a tile layer to the map
const tiles = L.tileLayer(
	"https://tile.openstreetmap.org/{z}/{x}/{y}.png",
	{
		maxZoom: 13,
		attribution:
			'&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
	}
).addTo(map);

      // Add any additional map configurations or markers here