const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Orders service is running'));

app.listen(3000, () => console.log('Orders service on port 3000'));

