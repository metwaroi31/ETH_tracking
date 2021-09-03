CREATE TABLE IF NOT EXISTS currency (
    currencyKey VARCHAR(10) NOT NULL,
  	lastModified DATETIME NOT NULL,
  	PRIMARY KEY(currencyKey)
);

CREATE TABLE IF NOT EXISTS platform (
	platformId VARCHAR(10) NOT NULL,
  	platformAddress VARCHAR(60) NOT NULL,
  	lastModified DATETIME NOT NULL,
  	PRIMARY KEY(platformId, platformAddress)
);

CREATE TABLE IF NOT EXISTS token (
	tokenId VARCHAR(10) NOT NULL,
  	name VARCHAR(20) NOT NULL,
  	symbol VARCHAR(20) NOT NULL,
  	lastModified DATETIME NOT NULL,
  	PRIMARY KEY(tokenId)
);

CREATE TABLE IF NOT EXISTS platformToken (
	tokenId VARCHAR(10) NOT NULL,
  	platformId VARCHAR(10) NOT NULL,
  	platformAddress VARCHAR(60) NOT NULL,
  	lastModified DATETIME NOT NULL,
  	PRIMARY KEY(tokenId, platformId, platformAddress)
);

CREATE TABLE IF NOT EXISTS exchangeRateRealtime (
	platformId VARCHAR(10) NOT NULL,
  	platformAddress VARCHAR(60) NOT NULL,
  	value REAL NOT NULL,
  	marketCap REAL NOT NULL,
  	volume REAL NOT NULL,
  	valueChange REAL NOT NULL,
  	lastUpdated DATETIME NOT NULL,
   	PRIMARY KEY(platformId, platformAddress),
  	FOREIGN KEY(platformId, platformAddress) references platform(platformId, platformAddress)
);

CREATE TABLE IF NOT EXISTS exchangeRateDaily (
	id INT IDENTITY(0,1) NOT NULL,
  	openValue REAL NOT NULL,
  	lowValue REAL NOT NULL,
  	highValue REAL NOT NULL,
  	closeValue REAL NOT NULL,
  	updatedDate DATETIME NOT NULL,
  	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS marketRateDaily (
	id INT IDENTITY(0,1) NOT NULL,
  	price REAL NOT NULL,
  	marketCap REAL NOT NULL,
  	totalVolume REAL NOT NULL,
  	updatedDate REAL NOT NULL,
  	PRIMARY KEY (id)
);