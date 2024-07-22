DROP TABLE IF EXISTS VRBO_dt;

CREATE TABLE VRBO_dt(
	Property_id VARCHAR, --make a unique id ourselves "Primary Key"
	Title VARCHAR,
	URL VARCHAR,
	Price INT,
	Total_price INT,
	lat VARCHAR,
	lng VARCHAR,
	LatLong VARCHAR,
	Rating VARCHAR,
	Rating_desc VARCHAR,
	Num_Reviews VARCHAR,	
	Check_in_Date VARCHAR, --Fields have dates but will need to be changed
	Check_out_Date VARCHAR, --Fields have dates but will need to be changed
	Destination VARCHAR,
	Room_type VARCHAR,
	NumPeople VARCHAR, --need to do conversions in pandas to number for blanks
	numbedroom VARCHAR, --need to do conversions in pandas to number
	numbathroom VARCHAR, --need to do conversions in pandas to number
	Source Varchar
	);


DROP TABLE IF EXISTS AirBNB_dt;

CREATE TABLE AirBNB_dt(
	Property_id VARCHAR, --make a unique id ourselves "Primary Key"
	Title VARCHAR,
	URL VARCHAR,
	Price INT,
	Total_price INT,
	lat VARCHAR,
	lng VARCHAR,
	LatLong VARCHAR,
	Rating VARCHAR,
	Rating_desc VARCHAR,
	Num_Reviews VARCHAR,	
	Check_in_Date VARCHAR, --Fields are blank
	Check_out_Date VARCHAR, --Fields are blank
	Destination VARCHAR,
	Room_type VARCHAR,
	NumPeople VARCHAR, --need to do conversions in pandas to number for blanks
	numbedroom VARCHAR, --need to do conversions in pandas to number
	numbathroom VARCHAR, --need to do conversions in pandas to number
	Source Varchar
	);