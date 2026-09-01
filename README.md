# candyspace-opal-poc
Proof of Concept for integrating an AI agent with external sales and marketing data.

# Building a Test Data DB
/data/data.zip = the test data from kaggle
/src-db/build_db.py = script to build an opal.db from the data in the data.zip archive
/src-db/test_db.py = a test script to query the DB.

## Execution (fresh terminal)
pip install -r requirements.txt
python src-db/build_db.py 
python src-db/test_db.py
python src-db/build_db.py --table <NAME>

Table names. customers, events, transactions, products, campaigns
