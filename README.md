# UNIR
Unresolved Network Issue Resolver

A small tool to expediate a tedious task. In our Network Operation Center (NOC), we track sites that have gone down in a database with a web interface. When a site comes back up, we manually have to click through three screens to resolve the issue. this is tiresome and time wasting.
<br>
So, instead, Virgil and I use a SQL query to resolve all the unresolved issues at once. Typing out the SQL code and running it on the server console eventually started to become tiresome as well.
<br>
Python to the rescue! I created a small GUI app to quickly enter the excluded sits (those still down) and run the SQL query.
Of course, you won't be able to connect to our server to test the app but you should be able to see what it is doing from the code and hopefully find something useful in it.
<br>
Virgil Hoover also contributed by writing the daymode/nightmode switching code (he loves his dark mode apps).
