CREATE TABLE loan.loan (
	id integer NOT NULL,
	actual TINYINT NOT NULL,
	predict TINYINT NOT NULL,
	`default` DOUBLE NOT NULL,
	none_default DOUBLE NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;
