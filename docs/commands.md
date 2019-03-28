## **commands:**
  
  * **display** (_Generates graphs and charts based on data from SQL database_)
    * table (_required_) `['call_statistics', 'suite_run_history']`
    * --db_type `[MySQL, PostgreSQL]` _default = MySQL_
  
  
  * **insert** (_Inserts csv data into the database_)
    * csv (_required_) `[path to csv file]`
    * db_type `['MySQL', PostgreSQL]` _default = MySQL_
    * --table `['call_statistics']` _default = 'call_statistics'_
  
  
  * **setup** (_Sets up database for use with tool_)
    * db_type (_required_) `[MySQL, PostgreSQL]` _default = MySQL_
    * --clear `[true, false]` _default = false_
  
  
  * **config** (_displays tool configuration_)
  
  
  * **--help** (_displays help_)
  
  * **--version** (_displays version_)