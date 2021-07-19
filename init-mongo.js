db = new Mongo().getDB("form-questions");

db.createUser({
  user: "root",
  pwd: "example",
  roles: ["readWrite", "dbAdmin"],
});
