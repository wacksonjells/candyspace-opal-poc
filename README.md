# candyspace-opal-poc
Proof of Concept for integrating an AI agent with external sales and marketing data.

# Building a Test Data DB
/data/data.zip = the test data from kaggle <br>
/src-db/build_db.py = script to build an opal.db from the data in the data.zip archive <br>
/src-db/test_db.py = a test script to query the DB. <br>

## Execution (fresh terminal)
pip install -r requirements.txt <br>
python src-db/build_db.py  <br>
python src-db/test_db.py <br>
python src-db/test_db.py --table \<NAME\> <br>

Table names. customers, events, transactions, products, campaigns <br>
