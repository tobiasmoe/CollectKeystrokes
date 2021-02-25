DROP TABLE IF EXISTS keystrokes;

CREATE TABLE keystrokes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_id INTEGER,
	session_id INTEGER,
	type BIT,
	key TEXT,
	keycode BIGINT,
	clocktime INTEGER,
	lastkey INTEGER
);
