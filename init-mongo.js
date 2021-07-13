db = new Mongo().getDB("form-questions");
db.createCollection("formQuestions", { capped: false });

db.createUser({
  user: "root",
  pwd: "example",
  roles: ["readWrite", "dbAdmin"],
});
