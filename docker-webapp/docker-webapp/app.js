const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
    res.send('<h1>Hello, World!</h1><p>This is my Docker container!</p>');
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
