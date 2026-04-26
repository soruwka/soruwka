const mineflayer = require('mineflayer');
const { SocksProxyAgent } = require('socks-proxy-agent');

// =========================== KONFIGURACJA ===========================
const HOST = "play.kaboom.pw";          // adres serwera
const PORT = 25565;                     // port
const BOT_COUNT = 50;                   // liczba botów
const SPAM_INTERVAL_MS = 10;          // interwał spamu (ms) – nie mniej niż 200-300
const SPAM_ENABLED = true;
const DELAY_BETWEEN_BOTS_MS = 3000;     // opóźnienie między botami
const MAX_RETRIES = 2;

const LOGIN_ENABLED = false;             // jeśli serwer wymaga /register i /login
const PASSWORD = "sraka123padaka";

const SERVER_VERSION = "1.21";           // wersja Minecrafta

// Lista wiadomości (stałe + dynamiczne kolory dla tytułu)
const SPAM_MESSAGES_STATIC = [
    "/say NIGGER",
    "/me 卍 NIGGER 卍",
    "/msg @a NIGGER",
    "卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER 卍 NIGGER ",
    "/kill @a",
    "/day",
    "/night",
    "/prefix &2&l[&a&lNIGGER_BOT_FUCK_THIS_SERVER&2&l]",
    "/prefix &9&l[&6&lNIGGER_BOT_FUCK_THIS_SERVER&9&l]",
    "/prefix &6&l[&5&lNIGGER_BOT_FUCK_THIS_SERVER&6&l]",
    "/particletrails ash",
    "/minecraft:op @s",
    "/title @a title {'text':'卍 NIGGER 卍','color':'red'}",
    "/kick @a"
];

// Lista dostępnych kolorów w Minecraft (dla JSON text component)
const COLORS = [
    "red", "blue", "green", "gold", "aqua", "light_purple", "yellow", "white",
    "dark_red", "dark_green", "dark_blue", "dark_aqua", "dark_purple", "gray", "dark_gray"
];

// Funkcja generująca losową wiadomość subtitle z losowym kolorem
function getRandomColorSubtitle() {
    const randomColor = COLORS[Math.floor(Math.random() * COLORS.length)];
    return `/title @a subtitle {'text':'FUCK NIGGERS, THEY SUCKS','color':'${randomColor}','bold':true}`;
}

// Funkcja zwracająca losową wiadomość ze stałej listy lub dynamiczny subtitle
function getRandomSpamMessage() {
    // 80% szans na losową wiadomość ze stałej listy, 20% na dynamiczny kolor subtitle
    if (Math.random() < 0.8) {
        const index = Math.floor(Math.random() * SPAM_MESSAGES_STATIC.length);
        return SPAM_MESSAGES_STATIC[index];
    } else {
        return getRandomColorSubtitle();
    }
}

// Lista proxy SOCKS5
const PROXY_LIST = [
    "socks5://sraxakaksa:123123haslo@31.59.20.176:6754",
    "socks5://sraxakaksa:123123haslo@198.23.239.134:6540",
    "socks5://sraxakaksa:123123haslo@45.38.107.97:6014",
    "socks5://sraxakaksa:123123haslo@107.172.163.27:6543",
    "socks5://sraxakaksa:123123haslo@198.105.121.200:6462",
    "socks5://sraxakaksa:123123haslo@216.10.27.159:6837",
    "socks5://sraxakaksa:123123haslo@142.111.67.146:5611",
    "socks5://sraxakaksa:123123haslo@191.96.254.138:6185",
    "socks5://sraxakaksa:123123haslo@31.58.9.4:6077",
    "socks5://sraxakaksa:123123haslo@104.239.107.47:5699"
];
// =====================================================================

function randomName() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let name = '';
    const length = Math.floor(Math.random() * 8) + 8;
    for (let i = 0; i < length; i++) name += chars.charAt(Math.floor(Math.random() * chars.length));
    return name;
}

function getProxyForBot(botNumber) {
    const index = (botNumber - 1) % PROXY_LIST.length;
    return PROXY_LIST[index];
}

function createBot(botNumber, retryCount = 1) {
    if (botNumber > BOT_COUNT) {
        console.log(`✅ Osiągnięto limit botów (${BOT_COUNT}). Kończę.`);
        return;
    }

    const botName = randomName();
    const proxyUrl = getProxyForBot(botNumber);
    const proxyLog = proxyUrl.replace(/:.+@/, ":****@");
    console.log(`\n[${botNumber}/${BOT_COUNT}] Próba ${retryCount}/${MAX_RETRIES} dla bota "${botName}"`);
    console.log(`  → Proxy: ${proxyLog}`);
    console.log(`  → Serwer: ${HOST}:${PORT}, wersja ${SERVER_VERSION}`);

    let spamInterval = null;
    let loginTimeout = null;
    let loginCompleted = false;
    let finished = false;

    const cleanupAndNext = (errorMsg, goToNextBot = true, retry = false) => {
        if (finished) return;
        finished = true;
        if (spamInterval) clearInterval(spamInterval);
        if (loginTimeout) clearTimeout(loginTimeout);

        if (retry && retryCount < MAX_RETRIES) {
            console.log(`[${botName}] ⚠️ ${errorMsg} – ponawiam za 5 sekund (próba ${retryCount+1}/${MAX_RETRIES})`);
            setTimeout(() => createBot(botNumber, retryCount + 1), 5000);
        } else if (goToNextBot) {
            console.log(`[${botName}] ❌ ${errorMsg || "Ostateczna porażka"} – przechodzę do następnego bota.`);
            setTimeout(() => createBot(botNumber + 1, 1), DELAY_BETWEEN_BOTS_MS);
        }
    };

    // Agent proxy
    let agent;
    try {
        agent = new SocksProxyAgent(proxyUrl);
        agent.timeout = 15000;
    } catch (err) {
        console.error(`[${botName}] Błąd tworzenia agenta proxy: ${err.message}`);
        cleanupAndNext("Nieprawidłowe proxy", true, false);
        return;
    }

    const bot = mineflayer.createBot({
        host: HOST,
        port: PORT,
        username: botName,
        version: SERVER_VERSION,
        auth: 'offline',
        agent: agent,
        keepAlive: true,
        checkTimeoutInterval: 30000
    });

    // Timeout na pojawienie się na serwerze
    loginTimeout = setTimeout(() => {
        if (!finished) {
            cleanupAndNext("Brak spawnu (timeout 30s)", true, true);
            if (bot._client) bot._client.end();
        }
    }, 30000);

    // Nasłuchiwanie odpowiedzi serwera (błędy komend, brak uprawnień)
    bot.on('message', (message) => {
        const text = message.toString();
        if (text.toLowerCase().includes('unknown command') || text.toLowerCase().includes('nie masz uprawnień')) {
            console.log(`[${botName}] 📩 Serwer odpowiedział: ${text.substring(0, 100)}`);
        }
    });

    bot.once('spawn', () => {
        if (finished) return;
        clearTimeout(loginTimeout);
        console.log(`[${botName}] ✅ Zalogowany i na serwerze!`);

        // Rejestracja/logowanie (jeśli włączone)
        if (LOGIN_ENABLED && !loginCompleted) {
            loginCompleted = true;
            console.log(`[${botName}] 🔐 Wysyłam /register ${PASSWORD}`);
            bot.chat(`/register ${PASSWORD} ${PASSWORD}`);

            const messageHandler = (message) => {
                const text = message.toString().toLowerCase();
                if (text.includes("already registered") || text.includes("already exists")) {
                    console.log(`[${botName}] ⚠️ Konto istnieje – wysyłam /login ${PASSWORD}`);
                    bot.chat(`/login ${PASSWORD}`);
                    bot.removeListener('message', messageHandler);
                } else if (text.includes("registered") || text.includes("success")) {
                    console.log(`[${botName}] ✅ Rejestracja udana!`);
                    bot.removeListener('message', messageHandler);
                } else if (text.includes("logged in")) {
                    console.log(`[${botName}] ✅ Zalogowano pomyślnie.`);
                    bot.removeListener('message', messageHandler);
                }
            };
            bot.on('message', messageHandler);
            setTimeout(() => bot.removeListener('message', messageHandler), 5000);
        }

        // Uruchom spam (z opóźnieniem, aby system logowania zdążył)
        if (SPAM_ENABLED) {
            setTimeout(() => {
                if (!finished && bot._client?.state === 'play') {
                    spamInterval = setInterval(() => {
                        if (bot._client?.state === 'play') {
                            const randomMsg = getRandomSpamMessage();
                            bot.chat(randomMsg);
                            console.log(`[${botName}] 📤 Wysłano: ${randomMsg}`);
                        }
                    }, SPAM_INTERVAL_MS);
                    console.log(`[${botName}] 🔁 Spam włączony (co ${SPAM_INTERVAL_MS} ms).`);
                }
            }, 3000);
        }

        // Uruchom następnego bota po opóźnieniu
        setTimeout(() => {
            if (!finished) {
                finished = true;
                createBot(botNumber + 1, 1);
            }
        }, DELAY_BETWEEN_BOTS_MS);
    });

    bot.on('error', (err) => {
        if (finished) return;
        console.log(`[${botName}] ❌ Błąd: ${err.message} (${err.code || ''})`);
        if (err.code === 'ECONNREFUSED') {
            cleanupAndNext(`Połączenie odrzucone – sprawdź proxy/serwer`, true, true);
        } else {
            cleanupAndNext(err.message, true, true);
        }
    });

    bot.on('end', (reason) => {
        if (finished) return;
        console.log(`[${botName}] Rozłączono: ${reason || 'nieznany powód'}`);
        cleanupAndNext(`Rozłączenie (${reason})`, true, true);
    });
}

// Start
console.log("🚀 Uruchamianie botów...");
createBot(1, 1);
