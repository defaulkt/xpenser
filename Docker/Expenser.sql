CREATE TABLE "expense" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "modified_at" timestamp,
  "account_id" int,
  "added_by" int,
  "modified_by" int,
  "category_id" int,
  "merchant_id" int,
  "tags" int[]
);

CREATE TABLE "category" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "recurring" bool,
  "mandatory" bool,
  "added_by" int,
  "parent_id" int,
  "child_id" int[],
  "created_at" timestamp
);

CREATE TABLE "users" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "email" varchar,
  "phone" varchar,
  "role_id" int
);

CREATE TABLE "account" (
  "id" SERIAL PRIMARY KEY,
  "bank_id" int,
  "name" varchar,
  "owner_id" int,
  "type" varchar,
  "last_transaction" int
);

CREATE TABLE "bank" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "active" bool
);

CREATE TABLE "merchants" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "category_id" int
);

CREATE TABLE "tags" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "added_by" int
);

COMMENT ON COLUMN "category"."parent_id" IS 'id of parent category';

COMMENT ON COLUMN "category"."child_id" IS 'id of child categories';

COMMENT ON COLUMN "account"."type" IS 'savings/checking';

ALTER TABLE "expense" ADD FOREIGN KEY ("category_id") REFERENCES "category" ("id");

ALTER TABLE "expense" ADD FOREIGN KEY ("added_by") REFERENCES "users" ("id");

ALTER TABLE "expense" ADD FOREIGN KEY ("modified_by") REFERENCES "users" ("id");

ALTER TABLE "category" ADD FOREIGN KEY ("added_by") REFERENCES "users" ("id");

ALTER TABLE "expense" ADD FOREIGN KEY ("account_id") REFERENCES "account" ("id");

ALTER TABLE "account" ADD FOREIGN KEY ("owner_id") REFERENCES "users" ("id");

ALTER TABLE "account" ADD FOREIGN KEY ("bank_id") REFERENCES "bank" ("id");

CREATE TABLE "expense_tags" (
  "expense_tags" int[] NOT NULL,
  "tags_id" int NOT NULL,
  PRIMARY KEY ("expense_tags", "tags_id")
);

ALTER TABLE "expense_tags" ADD FOREIGN KEY ("expense_tags") REFERENCES "expense" ("tags");

ALTER TABLE "expense_tags" ADD FOREIGN KEY ("tags_id") REFERENCES "tags" ("id");


ALTER TABLE "tags" ADD FOREIGN KEY ("added_by") REFERENCES "users" ("id");

ALTER TABLE "account" ADD FOREIGN KEY ("last_transaction") REFERENCES "expense" ("id");

ALTER TABLE "merchants" ADD FOREIGN KEY ("category_id") REFERENCES "category" ("id");

ALTER TABLE "expense" ADD FOREIGN KEY ("merchant_id") REFERENCES "merchants" ("id");
