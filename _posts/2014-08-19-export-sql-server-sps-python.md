---
layout: post
title: Export SQL Server Stored Procedures using Python
date: 2014-08-19T08:59:50-05:00
excerpt: 'The following short Python 2.7 script creates an export of all the stored procedures and functions within a SQL Server database.'
permalink: 2014/08/export-sql-server-sps-python/
tags:
  - Python
  - Sql Server
---
The following short Python 2.7 script creates an export of all the stored procedures and functions within a SQL Server database. This will export each procedure as a CREATE PROCEDURE or CREATE FUNCTION statement. The code uses [PyODBC](https://code.google.com/p/pyodbc/) to connect to the installation of SQL Server.

{% highlight python %}
import pyodbc, time

# Database configuration
dbServer = "" # The database server to connect to
db = "" # The database to connect to
uid = "" # The user
pwd = "" # The password
connString = """
              driver={SQL Server};
              server=""" + dbServer + """;
              database=""" + db + """;
              user id=""" + uid + """;
              password=""" + pwd + """;
             """
dateStr = time.strftime("%Y-%m-%d")
fileName = dbServer + "-" + db + "-" + dateStr + "-procedures.sql"
# i.e. TESTSERVER-TESTDB-2014-08-19-procedures.sql

# Connect to the database
conn = pyodbc.connect(connString)
cursor = conn.cursor()

##
# Export a stored procedure using its name and connected cursor
#
# @param string name: The name of the procedure to export
# @return string
##
def exportProcedure(name):
    sql = "EXEC sp_helptext N'" + name + "';"
    cursor.execute(sql)
    rows1 = cursor.fetchall()
    content = ""
    for r in rows1:
        content += r.Text.strip() + "\n"
    return content
"""
sysobjects contains different types of objects
-- P is a procedure
-- If the type contains F then it is a function
-- V is a view
-- U is a table
category = 0 indicates it is user-created
"""

# Get a list of system objects sorted by views, tables, procedures, and functions created by the user
content = ""
sql = "SELECT * FROM sysobjects WHERE (type LIKE '%F%' OR type = 'V' OR type = 'U' OR type='P') AND category = 0 ORDER BY type DESC, name"
cursor.execute(sql)
rows = cursor.fetchall()

# Export each of the stored procedures and functions
for r in rows:
    if r.type.strip() == "P" or "F" in r.type.strip():
        content += exportProcedure(r.name) + "\n\n"

# Write out the content
f = open(fileName, "w")
f.write(content)
f.close()
conn.close()
{% endhighlight %}