---
layout: post
permalink: "2014/12/passing-xml-to-sql-server/"
title: "Passing XML to Sql Server"
date: 2014-12-22T13:45:54-06:00
tags:
  - .NET
  - MS SQL
  - XML
---

One may want to pass an array of data to SQL Server. The most recent reason for me was so I could look for a specific record based on multiple criteria.

There are several ways to pass XML to SQL Server. One of the simplest ways to pass the data is as a string. However other options are available such as creating an SqlXML object from a list using the following C# function from

{% highlight ruby %}
/**
 * Get an SqlXml representation of the list
 *
 * @param IEnumerable list: The list to convert
 * @return SqlXml
 **/
public static SqlXml GetSqlXml(IEnumerable list)
{
    //We don't use 'using' or dispose or close the stream,
    //since it lives in the return variable
    MemoryStream stream = new MemoryStream();
    using (XmlWriter writer = XmlWriter.Create(stream))
    {
        writer.WriteStartElement("list");
        foreach (object obj in list)
        {
            writer.WriteElementString("item", obj.ToString());
        }
        writer.WriteEndElement();
        stream.Position = 0;
        return new SqlXml(stream);
    }
}
{% endhighlight %}

From: [http://www.codeproject.com/Articles/20847/Passing-Arrays-in-SQL-Parameters-using-XML-Data-Ty](http://www.codeproject.com/Articles/20847/Passing-Arrays-in-SQL-Parameters-using-XML-Data-Ty)

Another way to create the XML representation, in VB.net, is to use the following:

{% highlight vb %}
Dim xmlDoc As New System.Xml.XmlDocument
Dim table As System.Xml.XmlElement = xmlDoc.CreateElement("table")
For Each child As String In New String() {"s1", "s2", "s3"}
    Dim id As System.Xml.XmlElement = xmlDoc.CreateElement("id")
    id.innerText = child
    table.AppendChild(id)
Next
xmlDoc.AppendChild(table)
{% endhighlight %}

Then pass the xmlDoc as a string. Once you have the parameter set up, you can define a stored procedure to accept an XML parameter such as the following:

{% highlight bash %}
CREATE PROCEDURE [dbo].[StoredProcedure1] ( @Criteria XML = NULL )
AS
BEGIN
    ...
END
{% endhighlight %}

The last important piece is to parse the XML in SQL Server. If you have the following XML:

{% highlight bash %}
<table>
    <id>1</id>
    <id>2</id>
    <id>3</id>
</table>
{% endhighlight %}

You can access the “id” nodes by using the following:

{% highlight bash %}
SELECT r.id.value('.', 'varchar(50)') AS ID
FROM @Criteria.nodes('/table/id') AS r(id)
{% endhighlight %}