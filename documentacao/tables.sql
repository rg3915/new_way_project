# tables.sql

CREATE TABLE "subscriptions_subscription" (
	"id" integer NOT NULL PRIMARY KEY,
	"firstname" varchar(100) NOT NULL,
	"lastname" varchar(100) NOT NULL,
	"cpf" varchar(11) NOT NULL UNIQUE,
	"date_of_birth" date NOT NULL,
	"email" varchar(75) NOT NULL,
	"phone" varchar(20) NOT NULL,
	"cell" varchar(20) NOT NULL,
	"address" varchar(150) NOT NULL,
	"complement" varchar(100),
	"district" varchar(100) NOT NULL,
	"city" varchar(100) NOT NULL,
	"uf" varchar(100) NOT NULL,
	"cep" varchar(8) NOT NULL,
	"created_at" datetime NOT NULL