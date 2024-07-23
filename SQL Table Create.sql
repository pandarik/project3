DROP TABLE IF EXISTS Vacation_Rental_DT;

CREATE TABLE Vacation_Rental_DT(
	Property_id VARCHAR, 
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
	Check_in_Date VARCHAR, 
	Check_out_Date VARCHAR, 
	Destination VARCHAR,
	Room_type VARCHAR,
	NumPeople VARCHAR, 
	numbedroom VARCHAR, 
	numbathroom VARCHAR,
	Source VARCHAR,
	PRIMARY KEY(Source , Title, Property_id )
);