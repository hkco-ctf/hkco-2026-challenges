const express = require('express');
const https = require('https');
const fs = require('fs');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');
const { v4: uuidv4 } = require('uuid');
const path = require('path');
const serveIndex = require('serve-index');

const app = express();
const PORT = 3000;
const SECRET_KEY = "-2e7T{&9f)@Fh<OT@a^+-N?e/";

const sslOptions = {
    key: fs.readFileSync(path.join(__dirname, 'key.pem')),
    cert: fs.readFileSync(path.join(__dirname, 'cert.pem'))
};

app.use(cookieParser());
app.use(express.static('public'));

const backupPath = path.join(__dirname, 'backup');
app.use('/backup', express.static(backupPath), serveIndex(backupPath, { 'icons': true }));

app.get('/api/get-token', (req, res) => {
    const uniqueSessionId = uuidv4();

    const guestData = {
        session_id: uniqueSessionId,
        user: "guest",
        admin: false,
        iat: Math.floor(Date.now() / 1000)
    };

    const token = jwt.sign(guestData, SECRET_KEY, { algorithm: 'HS256' });

    res.cookie('auth_token', token, {
        httpOnly: false,
        secure: true,
        sameSite: 'none',
        path: '/',
        maxAge: 3600000
    });

    res.json({ message: "Success" });
});

app.get('/api/s3cr3t-p0r7al-f0r-adm1n', (req, res) => {
    const token = req.cookies.auth_token;

    if (!token) return res.status(401).json({ error: "No session token found." });

    try {
        const parts = token.split('.');
        const header = JSON.parse(Buffer.from(parts[0], 'base64').toString());
        const payload = JSON.parse(Buffer.from(parts[1], 'base64').toString());

        const content = jwt.verify(token, SECRET_KEY);
        if (content.admin === true) {
            return res.json({ flag: "hkco2026{g3tt1ng_th3_fl4g_by_s1gn1ng_y0ur_0wn_t0k3n}" });
        }
        
        res.status(403).json({ error: "Access Denied: Admin privileges required." });
    } catch (err) {
        res.status(400).json({ error: "Invalid Token." });
    }
});

https.createServer(sslOptions, app).listen(PORT, () => {
});